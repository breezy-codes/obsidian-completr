"""
Script to parse callouts from callouts.css and generate the TypeScript function for default callout options.

This can be used to modify the callouts offered by the plugin based on a custom CSS file.

Simply paste your custom.css file into the main project directory as callouts.css and run this script from the command line with `python updatecallouts.py`.

Take the output of the function and replace the function at the very end of the file called `callout_provider.ts` which is in the `src/provider` directory.
"""



import re

# Map RGB variable names to hex codes
rgb_to_hex = {
    "var(--drac-pink-rgb)": "#ff79c6",
    "var(--drac-cyan-rgb)": "#84def0",
    "var(--drac-purple-rgb)": "#bd93f9",
    "var(--drac-green-rgb)": "#50fa7b",
    "var(--drac-yellow-rgb)": "#f1fa8c",
    "var(--drac-red-rgb)": "#ff5555",
}

# Your default callouts
default_callouts = [
    ("Note", "note", "lucide-pencil", "#448aff"),
    ("Summary", "summary", "lucide-clipboard-list", "#00b0ff"),
    ("Abstract", "abstract", "lucide-clipboard-list", "#00b0ff"),
    ("TL;DR", "tldr", "lucide-clipboard-list", "#00b0ff"),
    ("Info", "info", "lucide-info", "#00b8d4"),
    ("To-Do", "todo", "lucide-check-circle-2", "#00b8d4"),
    ("Tip", "tip", "lucide-flame", "#00bfa6"),
    ("Hint", "hint", "lucide-flame", "#00bfa6"),
    ("Important", "important", "lucide-flame", "#00bfa6"),
    ("Success", "success", "lucide-check", "#00c853"),
    ("Check", "check", "lucide-check", "#00c853"),
    ("Done", "done", "lucide-check", "#00c853"),
    ("Question", "question", "lucide-help-circle", "#63dd17"),
    ("Help", "Help", "lucide-help-circle", "#63dd17"),
    ("FAQ", "faq", "lucide-help-circle", "#63dd17"),
    ("Warning", "warning", "lucide-alert-triangle", "#ff9100"),
    ("Caution", "caution", "lucide-alert-triangle", "#ff9100"),
    ("Attention", "attention", "lucide-alert-triangle", "#ff9100"),
    ("Failure", "failure", "lucide-x", "#ff5252"),
    ("Fail", "fail", "lucide-x", "#ff5252"),
    ("Missing", "missing", "lucide-x", "#ff5252"),
    ("Danger", "danger", "lucide-zap", "#ff1744"),
    ("Error", "error", "lucide-zap", "#ff1744"),
    ("Bug", "bug", "lucide-bug", "#f50057"),
    ("Example", "example", "lucide-list", "#7c4dff"),
    ("Quote", "quote", "quote-glyph", "#9e9e9e"),
    ("Cite", "cite", "quote-glyph", "#9e9e9e"),
]

css_path = "callouts.css"

with open(css_path, "r") as f:
    css = f.read()

pattern = re.compile(
    r'\.callout\[data-callout\^="([^"]+)"\][^{]*\{([^}]+)\}', re.MULTILINE
)

callouts = {}
for match in pattern.finditer(css):
    type_ = match.group(1)
    body = match.group(2)
    icon_match = re.search(r'--callout-icon:\s*([^;]+);', body)
    color_match = re.search(r'--callout-color:\s*([^;]+);', body)
    icon = icon_match.group(1).strip().strip('"') if icon_match else ""
    color_var = color_match.group(1).strip() if color_match else ""
    color = rgb_to_hex.get(color_var, color_var)
    # Overwrite or add
    callouts[type_.lower()] = (type_, type_, icon, color)

# Build final callout list, overwriting defaults if present in CSS
callout_dict = {replacement.lower(): (display, replacement, icon, color) for display, replacement, icon, color in default_callouts}
for k, v in callouts.items():
    callout_dict[k] = v

# Sort for consistency
final_callouts = sorted(callout_dict.values(), key=lambda x: x[0].lower())

# Generate the function
print("function generateDefaulCalloutOptions(): Suggestion[] {")
print("    const NOTE: [string, string] = ['lucide-pencil', '#448aff'];")
print("    const ABSTRACT: [string, string] = ['lucide-clipboard-list', '#00b0ff'];")
print("    const INFO: [string, string] = ['lucide-info', '#00b8d4'];")
print("    const TODO: [string, string] = ['lucide-check-circle-2', '#00b8d4'];")
print("    const TIP: [string, string] = ['lucide-flame', '#00bfa6'];")
print("    const SUCCESS: [string, string] = ['lucide-check', '#00c853'];")
print("    const QUESTION: [string, string] = ['lucide-help-circle', '#63dd17'];")
print("    const WARNING: [string, string] = ['lucide-alert-triangle', '#ff9100'];")
print("    const FAILURE: [string, string] = ['lucide-x', '#ff5252'];")
print("    const DANGER: [string, string] = ['lucide-zap', '#ff1744'];")
print("    const BUG: [string, string] = ['lucide-bug', '#f50057'];")
print("    const EXAMPLE: [string, string] = ['lucide-list', '#7c4dff'];")
print("    const QUOTE: [string, string] = ['quote-glyph', '#9e9e9e'];")
print("")
print("    return [")
for display, replacement, icon, color in final_callouts:
    # Use the const if available, else inline icon/color
    const_map = {
        "note": "NOTE",
        "summary": "ABSTRACT",
        "abstract": "ABSTRACT",
        "tldr": "ABSTRACT",
        "info": "INFO",
        "todo": "TODO",
        "tip": "TIP",
        "hint": "TIP",
        "important": "TIP",
        "success": "SUCCESS",
        "check": "SUCCESS",
        "done": "SUCCESS",
        "question": "QUESTION",
        "help": "QUESTION",
        "faq": "QUESTION",
        "warning": "WARNING",
        "caution": "WARNING",
        "attention": "WARNING",
        "failure": "FAILURE",
        "fail": "FAILURE",
        "missing": "FAILURE",
        "danger": "DANGER",
        "error": "DANGER",
        "bug": "BUG",
        "example": "EXAMPLE",
        "quote": "QUOTE",
        "cite": "QUOTE",
    }
    key = replacement.lower()
    if key in const_map:
        print(f'        newSuggestion("{display}", "{replacement}", ...{const_map[key]}),')
    else:
        print(f'        newSuggestion("{display}", "{replacement}", "{icon}", "{color}"),')
print("    ];")
print("}")