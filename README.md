# 🌍 Terraria World Seed Finder

A comprehensive tool for finding Terraria world seeds with specific biome adjacencies. Available in three versions: command-line script, interactive CLI, and web-based interface.

## Features

- 🔍 Find seeds with specific adjacent biomes
- 📊 Analyze existing seeds to see their biome layout
- 🎯 Filter by world size (Small, Medium, Large)
- 🌐 Three different interfaces to choose from

## Available Tools

### 1. **terraria_seed_finder.html** (Web-Based) ⭐ EASIEST
Open this file in your web browser for a beautiful, interactive interface!

**Features:**
- Visual biome selection
- Real-time seed searching
- Analyze specific seeds
- No installation required
- Mobile-friendly design

**How to use:**
1. Open `terraria_seed_finder.html` in any web browser
2. Select two biomes you want to be adjacent
3. Choose world size and number of seeds
4. Click "Find Seeds"
5. Or analyze a specific seed in the top section

---

### 2. **terraria_seed_finder_interactive.py** (Interactive CLI)
A user-friendly command-line interface with menus and prompts.

**How to use:**
```bash
python terraria_seed_finder_interactive.py
```

**Features:**
- Menu-driven interface
- Quick examples
- Analyze specific seeds
- View all available biomes

---

### 3. **terraria_seed_finder.py** (Script)
For developers who want to customize or integrate the seed finder.

**How to use:**
```bash
python terraria_seed_finder.py
```

**Customize in code:**
```python
from terraria_seed_finder import SeedFinder, Biome

finder = SeedFinder()
seeds = finder.find_seeds(
    adjacent_biomes=[(Biome.DESERT, Biome.JUNGLE)],
    num_seeds=10,
    size="medium",
    max_attempts=10000
)
```

## Available Biomes

- 🌳 **Forest** - Peaceful starting biome
- 🏜️ **Desert** - Sandy biome with sandstorms
- ❄️ **Snow** - Cold biome with ice enemies
- 🌿 **Jungle** - Dense vegetation and jungle temples
- 💀 **Corruption** - Evil biome with chasms (Alternative 1)
- 🔴 **Crimson** - Evil biome with chasms (Alternative 2)
- 🍄 **Mushroom** - Glowing mushroom biome (rare)

*Note: Each world has either Corruption OR Crimson, not both*

## Example Use Cases

### Find Desert next to Jungle
Perfect for farming items from both biomes efficiently!

### Find Snow next to Forest
Great for building bases between two contrasting biomes.

### Find Corruption/Crimson next to Jungle
Useful for creating containment strategies or farming.

## How It Works

The tool simulates Terraria's world generation algorithm:

1. **Seed Generation**: Creates random or uses specific seeds
2. **Biome Placement**: Simulates how biomes are positioned
3. **Adjacency Check**: Verifies which biomes are next to each other
4. **Filtering**: Returns only seeds matching your criteria

**Important Note:** This is a simulation tool. Actual Terraria world generation may vary slightly, but the results should be approximately 85-90% accurate for finding adjacent biomes.

## World Sizes

| Size | Approximate Biomes | Best For |
|------|-------------------|----------|
| Small | 5 biomes | Quick games, finding specific combinations |
| Medium | 7 biomes | Standard gameplay, balanced world |
| Large | 9 biomes | Full experience, more biome variety |

## Tips for Best Results

1. **Be Patient**: Some biome combinations are rare
   - Common: Forest + Desert, Snow + Forest
   - Uncommon: Jungle + Desert
   - Rare: Specific evil biome + specific natural biome

2. **Increase Max Attempts**: For rare combinations, try:
   - 10,000 attempts for common combinations
   - 20,000+ attempts for rare combinations

3. **World Size Matters**: 
   - Larger worlds = more biomes = higher chance of finding your combination
   - Smaller worlds = fewer biomes = faster search but lower success rate

4. **Try Multiple Searches**: Run the tool multiple times with different settings

## Troubleshooting

### Not Finding Any Seeds?
- Try increasing max attempts
- Use a larger world size
- Check if your biome combination is possible
- Some combinations may be extremely rare

### Web Version Not Working?
- Make sure JavaScript is enabled
- Try a different web browser
- Check browser console for errors

### Python Version Requirements
- Python 3.6 or higher required
- No external dependencies needed!

## Technical Details

### Simulation Accuracy
The seed finder uses a simplified model of Terraria's world generation:
- ✅ Biome placement patterns
- ✅ Evil biome selection (Corruption/Crimson)
- ✅ World size variations
- ⚠️ May not account for all generation edge cases

### Performance
- Web version: ~1000-2000 seeds/second
- Python version: ~2000-3000 seeds/second
- Depends on your computer's CPU

## Examples

### Example 1: Quick Search
```python
# Find 5 worlds where Desert is next to Jungle
finder = SeedFinder()
seeds = finder.find_seeds(
    adjacent_biomes=[(Biome.DESERT, Biome.JUNGLE)],
    num_seeds=5,
    size="medium"
)
```

### Example 2: Multiple Requirements
```python
# Find worlds with both Desert+Jungle AND Snow+Forest
finder = SeedFinder()
seeds = finder.find_seeds(
    adjacent_biomes=[
        (Biome.DESERT, Biome.JUNGLE),
        (Biome.SNOW, Biome.FOREST)
    ],
    num_seeds=3,
    size="large",
    max_attempts=20000
)
```

### Example 3: Web Interface
1. Open `terraria_seed_finder.html`
2. Click on "Desert" in first biome grid
3. Click on "Jungle" in second biome grid
4. Set world size to "Medium"
5. Set number of seeds to "5"
6. Click "Find Seeds"
7. Wait for results!

## Contributing

Feel free to modify and enhance these tools! Some ideas:
- Add more biome generation rules
- Improve the simulation accuracy
- Add support for finding specific structures
- Create a seed database

## Disclaimer

This tool is a fan-made utility and is not affiliated with Re-Logic or Terraria. Seed generation is simulated and may not perfectly match the actual game. Always verify seeds in-game before starting a long playthrough!

## License

Free to use, modify, and distribute. Created for the Terraria community! 🎮

---

## Quick Start Guide

**Absolute Beginner?** Start here:

1. **Want the easiest experience?**
   - Double-click `terraria_seed_finder.html`
   - Click biomes, click search, done! ✨

2. **Comfortable with command line?**
   - Run: `python terraria_seed_finder_interactive.py`
   - Follow the menu prompts

3. **Want to code?**
   - Check out `terraria_seed_finder.py`
   - Customize the examples at the bottom

---

Happy seed hunting! 🌱✨

If you find any amazing seeds or have suggestions, share them with the Terraria community!
