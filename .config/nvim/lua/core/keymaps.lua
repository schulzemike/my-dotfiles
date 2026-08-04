vim.g.mapleader = " "

local keymap = vim.keymap
-- ...
vim.keymap.set("n", "<leader>fj", "<cmd>%!jq .<CR>", opts)

vim.keymap.set('i', '<Space>ok', '✅', { noremap = true })
vim.keymap.set('i', '<Space>no', '❌', { noremap = true })
