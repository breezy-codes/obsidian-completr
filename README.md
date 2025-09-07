# Completr

[![](https://img.shields.io/github/v/release/breezy-codes/obsidian-completr?style=flat-square)](https://github.com/tth05/obsidian-completr/releases)
![](https://img.shields.io/github/downloads/breezy-codes/obsidian-completr/total?style=flat-square)

This plugin provides advanced auto-completion functionality for obsidian. Legacy editor not supported.

## Fork-specific Features by @breezy-codes

This repository is a fork of the original Completr project, with enhanced support for custom callout options. You can personalize the callout styles to match your own CSS preferences, allowing for a more tailored experience in Obsidian.

### How to Customize Callouts

1. **Edit Your CSS File**  
  Prepare your custom callout styles in a CSS file. This file should define the appearance and behavior of your callouts.

2. **Update Callouts Using `updatecallouts.py`**  
  Use the provided `updatecallouts.py` script to apply your custom styles. The script reads your CSS file and updates the plugin's callout configuration accordingly.  
  - Refer to the comments and instructions within `updatecallouts.py` for details on usage and required file paths.

3. **Modify `manifest.json`**  
  After updating your callouts, open the `manifest.json` file and ensure the repository URL and other metadata point to your fork. This helps users and Obsidian identify your customized version.

4. **Commit Your Changes**  
  Stage and commit all modified files to your repository:
  ```sh
  git add .
  git commit -m "Update callouts and manifest for custom fork"
  ```

5. **Tag and Release Your Fork**  
  Create a new release by tagging your commit and pushing the tag to GitHub:
  ```sh
  git tag v1.0.0
  git push origin v1.0.0
  ```
  Adjust the version number as needed for subsequent releases.

6. **Manual Installation in Obsidian**  
  Follow the manual installation steps described below to install your forked plugin in Obsidian:
  - Download the updated `main.js`, `styles.css`, and `manifest.json` from your release.
  - Copy these files into your vault's `.obsidian/plugins/obsidian-completr/` directory.

### Notes

- Custom callouts allow you to visually distinguish important information, warnings, tips, and more within your notes.
- If you encounter issues with callout rendering, double-check your CSS syntax and ensure the plugin is enabled in Obsidian.
- For advanced customization, you may further modify the plugin code or contribute improvements via pull requests.

By following these steps, you can maintain a personalized version of Completr with your own callout styles and easily distribute updates through GitHub releases.

## Features

- Latex support
    - No need to start with a `\`
    - Includes all MathJax commands
    - Allows `\begin...` completion for all environments
    - Support for inserting snippets with placeholders
- YAML Front Matter support
    - Learns any key with any value and provides completions for them
- Word list support
    - Load files where each line is a word
    - Performant, even with very big [lists](#looking-for-word-lists)
- Scanning your vault for words
    - Scans the current file or your whole vault to find new words which can then be suggested

## Installation

### Community plugin list

Browse the community plugins list and search for `Completr`.

### Manually

- Download `main.js, styles.css` and `manifest.json` from a release of your choice
- Copy the three files to your vault `VaultFolder/.obsidian/plugins/obsidian-completr/`

### After installation

1. Restart obsidian to ensure internal hooks can get registered properly
2. Check out the [hotkeys](#hotkeys) section to further configure the plugin

## Configuration

### Blacklist

- You can blacklist any suggestion by adding it to the `.obsidian/plugins/obsidian-completr/blacklisted_suggestions.txt`
  file
- Alternatively, you can use the hotkey to blacklist the currently selected suggestion (Default `Shift+D`)

### LaTeX commands

- All default LaTeX commands can be found in the `.obsidian/plugins/obsidian-completr/latex_commands.json` file
- You can add, remove or modify commands by editing this file
- Replacement syntax
    - `#` is a placeholder for snippets
    - `~` marks the cursor position to jump to. This cannot be on the same line as a placeholder
    - `\n` is a newline
- If the file contains incorrect syntax, a notice will pop up and the console will contain a more detailed error message

### Hotkeys

- All hotkeys are changeable from the hotkeys settings page
- The "bypass" hotkeys are useful to run actions which pretend that the popup isn't open.
    - If for example your insertion key is `Enter`, you couldn't press enter to go to the next line while the popup is
      open. This is where you could use the bypass key.
    - This also allows for other modifiers to be used, for example pressing `Tab` might require holding `Shift` to move
      backwards. Only modifiers which are not used in the bypass keybinding will be forwarded.
    - Note: The default bypass hotkeys might be shadowed by a built-in command. Check your keybindings if they don't
      work.
- If you want to change a hotkey without using any modifier, you need to use a workaround which can be
  found [here](https://forum.obsidian.md/t/be-able-of-using-the-function-keys-f1-f12-to-perform-functions/15748/7)
  or [here](https://forum.obsidian.md/t/function-keys-cant-be-bound-as-hotkeys-without-modifiers/26956/4), as Obsidian
  currently does not support this.

## Example usage

#### Latex snippets

![Latex](https://user-images.githubusercontent.com/36999320/146680089-57390cd7-e3c3-418c-9c55-9536259bb956.gif)

#### YAML Front Matter

![Front matter](https://user-images.githubusercontent.com/36999320/148700639-6cb48631-0b2f-45b8-b48a-40357425e8bf.gif)

#### File scanning

![File scanner](https://user-images.githubusercontent.com/36999320/146680134-33d8393b-956a-4028-ab2f-62526f76984d.gif)

#### Two million german words loaded

![Word list](https://user-images.githubusercontent.com/36999320/146680359-ae572473-8919-4927-a6f5-bc39800a5c23.gif)

## Looking for word lists?

- https://sourceforge.net/projects/germandict/
- https://github.com/kpym/FrequencyDictionaries

## Development

- Clone the repo to the `plugins` folder of an obsidian vault
- Run `npm i` and `npm run dev`
- Enable the plugin in obsidian
