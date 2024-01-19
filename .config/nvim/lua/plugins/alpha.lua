return {
    "goolord/alpha-nvim",
    dependencies = { "nvim-tree/nvim-web-devicons" },
    config = function ()
        require"alpha".setup(require"alpha.themes.startify".config)

        --
        -- keymap
        --
        local keymap = vim.keymap

        keymap.set("n", "<leader>h", ":Alpha<CR>")
    end
}
