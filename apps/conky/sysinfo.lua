conky.config = {
    background = true,
    update_interval = 1,
    total_run_times = 0,
    no_buffers = true,
    double_buffer = true,
    cpu_avg_samples = 2,
    net_avg_samples = 1,
	diskio_avg_samples = 10,

    alignment = 'top_right',
    gap_x = 130,
    gap_y = 110,

    -- minimum_height = 180,
    minimum_width = 400,
    -- maximum_width = 700,

    draw_shades = false,
    draw_outline = false,
    draw_borders = false,
    draw_graph_borders = true,

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
	color0 = '#00ffff',
	color1 = '#264653',

}

conky.text = [[
    ${offset 18}${font Cascadia Code:pixelsize=23}${color0}------------- ${font Cascadia Code:pixelsize=23}${color0}SYSTEM${font Cascadia Code:pixelsize=23}${color0} --------------
    ${offset -20}${font Cascadia Code:pixelsize=15}${color0}$sysname $kernel $alignr $machine
    ${offset -5}${font Cascadia Code:pixelsize=15}Date $alignr${time %A, %B %e}
    ${offset -5}${font Cascadia Code:pixelsize=15}Uptime $alignr${uptime_short}

    ${offset -2}${font Cascadia Code:pixelsize=23}${color0}------------- ${font Cascadia Code:pixelsize=23}${color0}NETWORK${font Cascadia Code:pixelsize=23}${color0} -------------
    ${offset -20}${font Cascadia Code:pixelsize=15}${color0}Private IP Address $alignr${addr wlp3s0}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}Public IP Address $alignr${offset 10}${execi 10 curl -s api.ipify.org} 
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}Down: $alignr${downspeed wlp3s0}
    ${offset -5}${downspeedgraph wlp3s0 20,455 #00ffff #00ffff}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}Up: $alignr${upspeed wlp3s0}
    ${offset -5}${upspeedgraph wlp3s0 20,455 #00ffff #00ffff}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}Downloaded: ${totaldown wlp3s0} ${alignr}${font Cascadia Code:pixelsize=15}${color0}Uploaded: ${totalup wlp3s0}

    ${font Cascadia Code:pixelsize=23}${color0}------------ ${font Cascadia Code:pixelsize=23}${color0}PROCESSORS${font Cascadia Code:pixelsize=23}${color0} -----------
    ${offset -20}${font Cascadia Code:pixelsize=15}${color0}Core1 ${cpu cpu1}% (${freq 1}MHz)${alignr}${cpubar cpu1 7, 260}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}Core2 ${cpu cpu2}% (${freq 2}MHz)${alignr}${cpubar cpu2 7, 260}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}Core3 ${cpu cpu3}% (${freq 3}MHz)${alignr}${cpubar cpu3 7, 260}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}Core4 ${cpu cpu4}% (${freq 4}MHz)${alignr}${cpubar cpu4 7, 260}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}Core5 ${cpu cpu5}% (${freq 5}MHz)${alignr}${cpubar cpu5 7, 260}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}Core6 ${cpu cpu6}% (${freq 6}MHz)${alignr}${cpubar cpu6 7, 260}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}Core7 ${cpu cpu7}% (${freq 7}MHz)${alignr}${cpubar cpu7 7, 260}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}Core8 ${cpu cpu8}% (${freq 8}MHz)${alignr}${cpubar cpu8 7, 260}

    ${font Cascadia Code:pixelsize=23}${color0}-------------- ${font Cascadia Code:pixelsize=23}${color0}MEMORY${font Cascadia Code:pixelsize=23}${color0} -------------
    ${offset -20}${font Cascadia Code:pixelsize=15}${color0}Read: $alignr${diskio_read}
    ${offset -5}${diskiograph_read 20,455 #00ffff #00ffff 750}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}Write: $alignr${diskio_write}
    ${offset -5}${diskiograph_write 20,455 #00ffff #00ffff 750}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}Ram: $mem/$memmax${alignr}${membar 7,250}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}/home: ${fs_used /home}/${fs_size /home}${alignr}${fs_bar 7,250}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}Swap: ${swap}/${swapmax}${alignr}${swapbar 7,250}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}Entropy: ${entropy_avail}/${entropy_poolsize}${alignr}${entropy_bar 7,250}

    ${font Cascadia Code:pixelsize=23}${color0}------------ ${font Cascadia Code:pixelsize=23}${color0}PROCESSES${font Cascadia Code:pixelsize=23}${color0} ------------
    ${offset -20}${font Cascadia Code:pixelsize=15}${color0}Total: $alignr${processes}
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}${top_mem name 1}$alignr${top cpu 1}% CPU ${top mem 1}% Ram
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}${top_mem name 2}$alignr${top cpu 2}% CPU ${top mem 2}% Ram
    ${offset -5}${font Cascadia Code:pixelsize=15}${color0}${top_mem name 3}$alignr${top cpu 3}% CPU ${top mem 3}% Ram
]]