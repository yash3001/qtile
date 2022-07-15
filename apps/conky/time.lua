conky.config = {
    background = true,
    update_interval = 1,
    total_run_times = 0,
    no_buffers = true,
    double_buffer = true,
    cpu_avg_samples = 2,
    net_avg_samples = 1,
	diskio_avg_samples = 10,

    alignment = 'top_left',
    gap_x = 100,
    gap_y = 400,

    minimum_height = 180,
    minimum_width = 5,
    maximum_width = 700,

    draw_shades = false,
    draw_outline = false,
    draw_borders = false,
    draw_graph_borders = false,

    own_window = true,
	own_window_class = 'Conky',
    own_window_type = 'override',
    own_window_transparent = true,
    own_window_hints = 'undecorated,below,sticky,skip_taskbar,skip_pager',
    own_window_colour = '#000000',
    own_window_argb_visual = false,
    own_window_argb_value = 0,
    
	format_human_readable = true,
    use_xft = true,
    xftalpha =  0.1,
    uppercase = false,
    override_utf8_locale = true,

    default_color = '#ffffff',
    default_shade_color = "#ff0000",
    default_outline_color = '#00ff00',
}

conky.text = [[
    ${voffset 10}${color #eaeaea}${font DaddyTimeMono Nerd Font:pixelsize=150}${time %I:%M}${voffset -65}${offset 30}${color #00ffff}${font DaddyTimeMono Nerd Font:pixelsize=42}${time %d}${offset 10}${voffset -8}${color EAEAEA}${font DaddyTimeMono Nerd Font:pixelsize=22}${time %B}${offset 10}${voffset 1}${time %Y}${font}${voffset 28}${font DaddyTimeMono Nerd Font:pixelsize=58}${offset -168}${time %A}
]]