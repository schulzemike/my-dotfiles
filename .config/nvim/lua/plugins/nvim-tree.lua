return {
    "nvim-tree/nvim-tree.lua",
    dependencies = {
        "nvim-tree/nvim-web-devicons"
    },
    config = function()
        local nvimtree = require("nvim-tree")

        -- Config values from the quick start guide found on the github page
        -- disable netrw at the very start of your init.lua
        vim.g.loaded_netrw = 1
        vim.g.loaded_netrwPlugin = 1

        nvimtree.setup({
            view = {
                width = 40,
            },
        })

        --
        -- keymap
        --
        local keymap = vim.keymap

        keymap.set("n", "<leader>e", ":NvimTreeToggle<CR>")
    end
}
