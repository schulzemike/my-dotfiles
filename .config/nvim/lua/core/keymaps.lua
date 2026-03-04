vim.g.mapleader = " "

local keymap = vim.keymap
-- ...
vim.keymap.set("n", "<leader>fj", "<cmd>%!jq .<CR>", opts)
