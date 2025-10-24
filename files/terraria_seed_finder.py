#!/usr/bin/env python3
"""
Terraria World Seed Finder
Finds seeds with specific biome adjacencies
"""

import random
import json
from dataclasses import dataclass
from typing import List, Set, Tuple
from enum import Enum

class Biome(Enum):
    """Available Terraria biomes"""
    FOREST = "Forest"
    DESERT = "Desert"
    SNOW = "Snow"
    JUNGLE = "Jungle"
    CORRUPTION = "Corruption"
    CRIMSON = "Crimson"
    OCEAN = "Ocean"
    DUNGEON = "Dungeon"
    MUSHROOM = "Mushroom"

@dataclass
class WorldConfig:
    """World generation configuration"""
    seed: str
    size: str  # small, medium, large
    evil: str  # corruption or crimson
    biomes: List[Tuple[Biome, int]]  # (biome, position)
    
    def has_adjacent_biomes(self, biome1: Biome, biome2: Biome) -> bool:
        """Check if two biomes are adjacent in this world"""
        positions = {biome: pos for biome, pos in self.biomes}
        if biome1 not in positions or biome2 not in positions:
            return False
        return abs(positions[biome1] - positions[biome2]) == 1

class TerrariaWorldGenerator:
    """Simulates Terraria world generation to analyze biome placement"""
    
    def __init__(self, seed: str = None, size: str = "medium"):
        self.seed = seed or str(random.randint(1000000000, 9999999999))
        self.size = size
        self.random = random.Random(self.seed)
        
    def generate_world(self) -> WorldConfig:
        """Generate a world layout based on seed"""
        # Determine world size
        if self.size == "small":
            num_biomes = 5
        elif self.size == "medium":
            num_biomes = 7
        else:  # large
            num_biomes = 9
        
        # Choose evil biome (corruption or crimson)
        evil = self.random.choice([Biome.CORRUPTION, Biome.CRIMSON])
        
        # Generate biome layout
        biomes = []
        
        # Always have ocean at edges (position 0 and last)
        biomes.append((Biome.OCEAN, 0))
        
        # Core biomes that always appear
        core_biomes = [Biome.FOREST, Biome.DESERT, Biome.SNOW, Biome.JUNGLE, evil]
        self.random.shuffle(core_biomes)
        
        # Add core biomes to positions
        for i, biome in enumerate(core_biomes[:num_biomes-2]):
            biomes.append((biome, i + 1))
        
        # Optional biomes for larger worlds
        if num_biomes > 7:
            if self.random.random() > 0.5:
                biomes.append((Biome.MUSHROOM, num_biomes - 2))
        
        # Ocean at the end
        biomes.append((Biome.OCEAN, num_biomes - 1))
        
        # Sort by position
        biomes.sort(key=lambda x: x[1])
        
        return WorldConfig(
            seed=self.seed,
            size=self.size,
            evil=evil.value,
            biomes=biomes
        )

class SeedFinder:
    """Finds seeds matching specific criteria"""
    
    def __init__(self):
        self.found_seeds = []
    
    def find_seeds(self, 
                   adjacent_biomes: List[Tuple[Biome, Biome]],
                   num_seeds: int = 10,
                   size: str = "medium",
                   max_attempts: int = 10000) -> List[WorldConfig]:
        """
        Find seeds with specific biome adjacencies
        
        Args:
            adjacent_biomes: List of biome pairs that should be adjacent
            num_seeds: Number of matching seeds to find
            size: World size (small, medium, large)
            max_attempts: Maximum number of seeds to try
        """
        found = []
        attempts = 0
        
        print(f"Searching for seeds with adjacent biomes: {[(b1.value, b2.value) for b1, b2 in adjacent_biomes]}")
        print(f"World size: {size}")
        print(f"Target: {num_seeds} seeds\n")
        
        while len(found) < num_seeds and attempts < max_attempts:
            attempts += 1
            
            # Generate random seed
            seed = str(random.randint(1000000000, 9999999999))
            generator = TerrariaWorldGenerator(seed, size)
            world = generator.generate_world()
            
            # Check if this world matches criteria
            matches = all(
                world.has_adjacent_biomes(biome1, biome2)
                for biome1, biome2 in adjacent_biomes
            )
            
            if matches:
                found.append(world)
                print(f"✓ Found seed #{len(found)}: {seed}")
                self._print_world_layout(world)
                print()
            
            if attempts % 1000 == 0:
                print(f"Searched {attempts} seeds... (found {len(found)})")
        
        if len(found) < num_seeds:
            print(f"\nWarning: Only found {len(found)} matching seeds after {attempts} attempts")
        else:
            print(f"\nSuccess! Found {len(found)} matching seeds after {attempts} attempts")
        
        return found
    
    def _print_world_layout(self, world: WorldConfig):
        """Print a visual representation of the world layout"""
        layout = " → ".join([f"{biome.value}" for biome, _ in world.biomes])
        print(f"  Layout: {layout}")
        print(f"  Evil Biome: {world.evil}")
    
    def save_results(self, filename: str = "found_seeds.json"):
        """Save found seeds to a JSON file"""
        data = []
        for world in self.found_seeds:
            data.append({
                "seed": world.seed,
                "size": world.size,
                "evil": world.evil,
                "biomes": [(b.value, pos) for b, pos in world.biomes]
            })
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Results saved to {filename}")


def main():
    """Main interactive interface"""
    print("=" * 60)
    print("TERRARIA WORLD SEED FINDER")
    print("=" * 60)
    print()
    
    # Example usage
    print("Example 1: Find worlds with Desert next to Jungle")
    print("-" * 60)
    finder = SeedFinder()
    seeds = finder.find_seeds(
        adjacent_biomes=[(Biome.DESERT, Biome.JUNGLE)],
        num_seeds=5,
        size="medium",
        max_attempts=5000
    )
    
    print("\n" + "=" * 60)
    print("\nExample 2: Find worlds with Snow next to Forest")
    print("-" * 60)
    finder2 = SeedFinder()
    seeds2 = finder2.find_seeds(
        adjacent_biomes=[(Biome.SNOW, Biome.FOREST)],
        num_seeds=5,
        size="large",
        max_attempts=5000
    )
    
    print("\n" + "=" * 60)
    print("\nExample 3: Multiple adjacency requirements")
    print("-" * 60)
    finder3 = SeedFinder()
    seeds3 = finder3.find_seeds(
        adjacent_biomes=[
            (Biome.DESERT, Biome.JUNGLE),
            (Biome.SNOW, Biome.FOREST)
        ],
        num_seeds=3,
        size="large",
        max_attempts=10000
    )
    
    print("\n" + "=" * 60)
    print("\nCUSTOM SEARCH")
    print("=" * 60)
    print("\nAvailable biomes:")
    for biome in Biome:
        if biome not in [Biome.OCEAN]:  # Ocean is always at edges
            print(f"  - {biome.value}")
    
    print("\nTo create your own search, modify the main() function with:")
    print("  finder.find_seeds(")
    print("      adjacent_biomes=[(Biome.YOUR_BIOME1, Biome.YOUR_BIOME2)],")
    print("      num_seeds=10,")
    print("      size='medium',  # small, medium, or large")
    print("      max_attempts=10000")
    print("  )")


if __name__ == "__main__":
    main()
