#!/usr/bin/env python3
"""
Interactive Terraria World Seed Finder
Easy-to-use CLI interface for finding seeds with specific biome adjacencies
"""

import random
from dataclasses import dataclass
from typing import List, Tuple, Optional
from enum import Enum


class Biome(Enum):
    """Available Terraria biomes"""
    FOREST = "Forest"
    DESERT = "Desert"
    SNOW = "Snow"
    JUNGLE = "Jungle"
    CORRUPTION = "Corruption"
    CRIMSON = "Crimson"
    MUSHROOM = "Mushroom"


@dataclass
class WorldConfig:
    """World generation configuration"""
    seed: str
    size: str
    evil: str
    biomes: List[Tuple[Biome, int]]
    
    def has_adjacent_biomes(self, biome1: Biome, biome2: Biome) -> bool:
        """Check if two biomes are adjacent"""
        positions = {biome: pos for biome, pos in self.biomes}
        if biome1 not in positions or biome2 not in positions:
            return False
        return abs(positions[biome1] - positions[biome2]) == 1
    
    def get_biome_layout(self) -> str:
        """Get a visual representation of biome layout"""
        return " → ".join([f"{biome.value}" for biome, _ in self.biomes])


class WorldGenerator:
    """Generates Terraria worlds from seeds"""
    
    def __init__(self, seed: str, size: str = "medium"):
        self.seed = seed
        self.size = size.lower()
        self.random = random.Random(int(seed) if seed.isdigit() else hash(seed))
        
    def generate(self) -> WorldConfig:
        """Generate world layout"""
        # Determine number of biome slots based on size
        size_map = {"small": 5, "medium": 7, "large": 9}
        num_slots = size_map.get(self.size, 7)
        
        # Choose evil biome
        evil = self.random.choice([Biome.CORRUPTION, Biome.CRIMSON])
        
        # Core biomes (always present)
        core_biomes = [Biome.FOREST, Biome.DESERT, Biome.SNOW, Biome.JUNGLE, evil]
        self.random.shuffle(core_biomes)
        
        # Build biome list with positions
        biomes = []
        current_pos = 0
        
        # Add biomes
        for biome in core_biomes[:num_slots]:
            biomes.append((biome, current_pos))
            current_pos += 1
        
        # Add mushroom for larger worlds occasionally
        if num_slots > 7 and self.random.random() > 0.6:
            biomes.append((Biome.MUSHROOM, current_pos))
        
        # Sort by position
        biomes.sort(key=lambda x: x[1])
        
        return WorldConfig(
            seed=self.seed,
            size=self.size,
            evil=evil.value,
            biomes=biomes
        )


class InteractiveSeedFinder:
    """Interactive seed finder with CLI interface"""
    
    def __init__(self):
        self.results = []
    
    def run(self):
        """Main interactive loop"""
        print("\n" + "=" * 70)
        print("🌍  TERRARIA WORLD SEED FINDER  🌍")
        print("=" * 70)
        print("\nFind Terraria world seeds with specific biome adjacencies!")
        
        while True:
            print("\n" + "-" * 70)
            print("\nOPTIONS:")
            print("  1. Find seeds with adjacent biomes")
            print("  2. Analyze a specific seed")
            print("  3. View available biomes")
            print("  4. Quick examples")
            print("  5. Exit")
            
            choice = input("\nSelect an option (1-5): ").strip()
            
            if choice == "1":
                self.find_seeds_interactive()
            elif choice == "2":
                self.analyze_seed()
            elif choice == "3":
                self.show_biomes()
            elif choice == "4":
                self.show_examples()
            elif choice == "5":
                print("\nThanks for using the Terraria Seed Finder! 👋")
                break
            else:
                print("❌ Invalid option. Please try again.")
    
    def show_biomes(self):
        """Display available biomes"""
        print("\n" + "=" * 70)
        print("AVAILABLE BIOMES")
        print("=" * 70)
        for i, biome in enumerate([b for b in Biome], 1):
            print(f"  {i}. {biome.value}")
        print("\n💡 Tip: Not all biomes appear in every world size!")
    
    def show_examples(self):
        """Show example searches"""
        print("\n" + "=" * 70)
        print("QUICK EXAMPLES")
        print("=" * 70)
        
        examples = [
            ("Desert next to Jungle", [(Biome.DESERT, Biome.JUNGLE)], "medium"),
            ("Snow next to Forest", [(Biome.SNOW, Biome.FOREST)], "large"),
            ("Corruption next to Jungle", [(Biome.CORRUPTION, Biome.JUNGLE)], "medium"),
        ]
        
        for i, (desc, biomes, size) in enumerate(examples, 1):
            print(f"\n{i}. {desc} (world size: {size})")
        
        choice = input("\nRun an example? (1-3, or press Enter to skip): ").strip()
        
        if choice in ["1", "2", "3"]:
            idx = int(choice) - 1
            desc, biomes, size = examples[idx]
            print(f"\n🔍 Searching for: {desc}")
            self._search(biomes, size, 5, 5000)
    
    def find_seeds_interactive(self):
        """Interactive seed finding"""
        print("\n" + "=" * 70)
        print("FIND SEEDS WITH ADJACENT BIOMES")
        print("=" * 70)
        
        # Select world size
        print("\nWorld size:")
        print("  1. Small")
        print("  2. Medium")
        print("  3. Large")
        size_choice = input("Select size (1-3, default: 2): ").strip() or "2"
        size_map = {"1": "small", "2": "medium", "3": "large"}
        size = size_map.get(size_choice, "medium")
        
        # Select biomes
        print("\nAvailable biomes:")
        biome_list = list(Biome)
        for i, biome in enumerate(biome_list, 1):
            print(f"  {i}. {biome.value}")
        
        print("\nEnter two biomes that should be adjacent:")
        biome1_idx = int(input(f"First biome (1-{len(biome_list)}): ").strip()) - 1
        biome2_idx = int(input(f"Second biome (1-{len(biome_list)}): ").strip()) - 1
        
        if 0 <= biome1_idx < len(biome_list) and 0 <= biome2_idx < len(biome_list):
            biome1 = biome_list[biome1_idx]
            biome2 = biome_list[biome2_idx]
            
            num_seeds = int(input("\nHow many seeds to find? (default: 5): ").strip() or "5")
            max_attempts = int(input("Maximum attempts? (default: 5000): ").strip() or "5000")
            
            print(f"\n🔍 Searching for {biome1.value} next to {biome2.value}...")
            self._search([(biome1, biome2)], size, num_seeds, max_attempts)
        else:
            print("❌ Invalid biome selection!")
    
    def analyze_seed(self):
        """Analyze a specific seed"""
        print("\n" + "=" * 70)
        print("ANALYZE SPECIFIC SEED")
        print("=" * 70)
        
        seed = input("\nEnter seed: ").strip()
        if not seed:
            print("❌ No seed entered!")
            return
        
        print("\nWorld size:")
        print("  1. Small")
        print("  2. Medium")
        print("  3. Large")
        size_choice = input("Select size (1-3, default: 2): ").strip() or "2"
        size_map = {"1": "small", "2": "medium", "3": "large"}
        size = size_map.get(size_choice, "medium")
        
        generator = WorldGenerator(seed, size)
        world = generator.generate()
        
        print(f"\n" + "=" * 70)
        print(f"SEED ANALYSIS: {seed}")
        print("=" * 70)
        print(f"World Size: {world.size.capitalize()}")
        print(f"Evil Biome: {world.evil}")
        print(f"\nBiome Layout:")
        print(f"  {world.get_biome_layout()}")
        print("\nAdjacent Biome Pairs:")
        for i in range(len(world.biomes) - 1):
            biome1, _ = world.biomes[i]
            biome2, _ = world.biomes[i + 1]
            print(f"  • {biome1.value} ↔ {biome2.value}")
    
    def _search(self, adjacent_biomes: List[Tuple[Biome, Biome]], 
                size: str, num_seeds: int, max_attempts: int):
        """Perform seed search"""
        found = []
        attempts = 0
        
        print(f"\nSearching... (target: {num_seeds} seeds)")
        
        while len(found) < num_seeds and attempts < max_attempts:
            attempts += 1
            
            seed = str(random.randint(1000000000, 9999999999))
            generator = WorldGenerator(seed, size)
            world = generator.generate()
            
            if all(world.has_adjacent_biomes(b1, b2) for b1, b2 in adjacent_biomes):
                found.append(world)
                print(f"\n✅ Found #{len(found)}: {seed}")
                print(f"   {world.get_biome_layout()}")
            
            if attempts % 500 == 0:
                print(f"   ... searched {attempts} seeds ({len(found)} found)")
        
        print(f"\n" + "=" * 70)
        if len(found) < num_seeds:
            print(f"⚠️  Found {len(found)}/{num_seeds} seeds after {attempts} attempts")
        else:
            print(f"✅ Success! Found {num_seeds} seeds after {attempts} attempts")
        
        if found:
            print("\nSEEDS FOUND:")
            for i, world in enumerate(found, 1):
                print(f"\n  {i}. Seed: {world.seed}")
                print(f"     Layout: {world.get_biome_layout()}")
                print(f"     Evil: {world.evil}")


def main():
    """Entry point"""
    finder = InteractiveSeedFinder()
    finder.run()


if __name__ == "__main__":
    main()
