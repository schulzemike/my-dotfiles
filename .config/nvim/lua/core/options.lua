local opt = vim.opt

opt.autowrite = true

-- backspace
opt.backspace = "indent,eol,start"

-- clipboard
opt.clipboard:append("unnamedplus")

-- cursor line & appearance
opt.cursorline = true
opt.guifont = {"JetBrainsMono MF", "h12"}
opt.termguicolors = true

-- consider '-' dash as a part of the word
opt.iskeyword:append("-")

-- line numbers
opt.number = true
opt.relativenumber = true
opt.numberwidth = 6

-- line wrapping
opt.wrap = false

-- search settings
opt.ignorecase = true
opt.smartcase = true

-- tab behaviour
opt.autoindent = true
opt.expandtab = true
opt.shiftwidth = 4
opt.softtabstop = 4
opt.tabstop = 4

