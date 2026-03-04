-- vim.pack.add({"https://github.com/ellisonleao/gruvbox.nvim"})
-- vim.cmd("colorscheme gruvbox")

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
