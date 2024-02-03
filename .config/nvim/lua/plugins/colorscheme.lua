return {
    -- "rebelot/kanagawa.nvim",
    -- lazy = false,
    -- priority = 1000,
    -- config = function()
    --     vim.cmd("colorscheme kanagawa")
    -- end,
    "ellisonleao/gruvbox.nvim",
    lazy = false,
    priority = 1000,
    config = function()

        local gruvbox = require("gruvbox")

        gruvbox.setup {
            contrast = "hard"
        }
        
        -- colorscheme command has to be called after setup
        vim.cmd("colorscheme gruvbox")
    end,
}
