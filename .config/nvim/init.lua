require("core.options")
require("core.keymaps")

vim.lsp.enable({"bashls", "lua_ls"})



vim.pack.add({
    "https://github.com/nvim-tree/nvim-web-devicons",
    "https://github.com/nvim-treesitter/nvim-treesitter",
    "https://github.com/neovim/nvim-lspconfig",
    "https://github.com/windwp/nvim-autopairs",
    "https://github.com/ellisonleao/gruvbox.nvim",
    "https://github.com/MeanderingProgrammer/render-markdown.nvim",
    "https://github.com/norcalli/nvim-colorizer.lua",
    "https://github.com/nvim-lualine/lualine.nvim",
    "https://github.com/vimwiki/vimwiki",
    "https://github.com/3rd/image.nvim",
    "https://github.com/3rd/diagram.nvim",
})




require("nvim-autopairs").setup()
require("colorizer").setup()

require('render-markdown').setup({
    file_types = { 'markdown', 'vimwiki' },
    heading = {
        -- icons = { '󰬺 ','󰬻 ','󰬼 ','󰬽 ','󰬾 ','󰬿 ' },
        width = { 'full','block','block','block','block','block' },
        min_width = 50,
        border = true,
    }
})

require("nvim-treesitter").setup({
    highlight = { enable = true },
    indent = { enable = true },
    ensure_installed = {
        "sql",
    },
})

require("lualine").setup({
    options = {
        theme = "gruvbox_dark",    
    }
})

vim.g.vimwiki_list = {
    {
        path = '~/vimwiki',
        syntax = 'markdown',
        ext = '.md',
    },
}

-- using the default config and the kitty backend
require("image").setup()

-- using the ueberzug++ backend
-- require("image").setup({
--     backend = "ueberzug"
-- })
require("diagram").setup({
    integrations = {
        require("diagram.integrations.markdown"),
    },
    renderer_options = {
        mermaid = {
            background = "transparent",
            theme = "dark",
        },
        plantuml = {
            charset = "utf-8",
        }
    }
})

vim.cmd("colorscheme gruvbox")
