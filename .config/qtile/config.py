from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, BorderDecoration

import fontawesome as fa

mod = "mod4" # Super key
terminal = guess_terminal()

keys = [
    # Window bindings
    Key([mod], "s", lazy.layout.left(),
        desc="Move focus to left"),
    Key([mod], "f", lazy.layout.right(),
        desc="Move focus to right"),
    Key([mod], "d", lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "e", lazy.layout.up(),
        desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    Key([mod], "w", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod], "r", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "control"], "d", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "control"], "s", lazy.layout.shuffle_up(),
        desc="Move window up"),
    Key([mod, "mod1"], "s", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "mod1"], "f", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "mod1"], "d", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "mod1"], "e", lazy.layout.grow_up(),
        desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(),
        desc="Reset all window sizes"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "g", lazy.window.toggle_floating(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Tab", lazy.next_layout(),
        desc="Toggle between layouts"),
    Key([mod, "control"], "r", lazy.restart(),
        desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(),
        desc="Shutdown Qtile"),
    Key([mod], "q", lazy.window.kill(),
        desc="Kill focused window"),

    # Spawn Bindings
    Key([mod], "y", lazy.spawn(terminal),
        desc="Launch terminal"),
    Key([mod], "Return", lazy.spawn('rofi -show drun'),
        desc="Run rofi"),
    Key([mod], "space", lazy.spawn('alacritty -e broot'),
        desc="Run Broot"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


# groups = [
#     # Group("1", 'G'),
#     Group("1", label=fa.icons["terminal"]),
#     Group("2", label=fa.icons["firefox"]),
#     Group("3", label=fa.icons["code"]),
#     Group("4", label=fa.icons["folder"]),
#     Group("5", label=fa.icons["github"]),
#     Group("6", label=fa.icons["soundcloud"]),
#     Group("7", label=fa.icons["gamepad"]),
#     # Group("8", label = fa.icons["firefox"]),
#     # Group("9", label = fa.icons["firefox"]),
# ]

# for i in groups:
#     keys.extend(
#         [
#             # mod1 + letter of group = switch to group
#             Key(
#                 [mod],
#                 i.name,
#                 lazy.group[i.name].toscreen(),
#                 desc="Switch to group {}".format(i.name),
#             ),
#             # mod1 + shift + letter of group = switch to & move focused window to group
#             Key(
#                 [mod, "shift"],
#                 i.name,
#                 lazy.window.togroup(i.name, switch_group=True),
#                 desc="Switch to & move focused window to group {}".format(
#                     i.name),
#             ),
#             # Or, use below if you prefer not to switch to that group.
#             # # mod1 + shift + letter of group = move focused window to group
#             # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#             #     desc="move focused window to group {}".format(i.name)),
#         ]
    # )

layouts = [
    layout.Columns(
        border_focus_stack=['#ffffff', '#ffffff'],
        border_focus="#ffffff",
        border_normal='#000000',
        border_width=7,
        margin = 8),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=22,
    markup=True,
    padding=15,
    foreground='#000000',
    rounded = True,
)
extension_defaults = widget_defaults.copy()

decor = {
    "decorations": [
        RectDecoration(colour="#f7f7f7", radius=5, filled=True, padding_y=0, padding_x=5),
    ],
    # "padding": 50,
    # "margin": 50,
}

padding = 6
screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.WindowName(
                    width=150,
                    decorations=[
                        RectDecoration(
                            colour="#ffffff",
                            radius=7,
                            filled=True,
                            padding_y=0,
                            padding_x=padding
                        ),
                    ]
                ),
                widget.Net(
                    background="#00000000",
                    format=fa.icons["wifi"]+" {up}", decorations=[
                        RectDecoration(
                            colour="#96cdfb",
                            radius=7,
                            filled=True,
                            padding_y=0,
                            padding_x=padding
                        ),
                    ]
                ),
                widget.Memory(background="#00000000",
                    measure_mem='G', format=fa.icons["server"] + "{MemUsed: .2f} GB", decorations=[
                        RectDecoration(
                            colour="#f8bd96",
                            radius=7,
                            filled=True,
                            padding_y=0,
                            padding_x=padding
                        ),
                    ]
                ),
                widget.CPU(format=fa.icons["microchip"]+" {load_percent}%", decorations=[
                        RectDecoration(
                            colour="#fae3b0",
                            radius=7,
                            filled=True,
                            padding_y=0,
                            padding_x=padding
                        ),
                    ]
                ),
                widget.Spacer(length=bar.STRETCH),
                widget.GroupBox(
                    disable_drag=True,
                    background="#f2cdcd",
                    active="#000000",
                    inactive="#7f7f7f",
                    highlight_method='line',
                    highlight_color="#00000000",
                    borderwidth=6,
                    # border="#000000",
                    decorations=[
                        RectDecoration(
                            radius=5,
                        )
                    ],
                ),
                widget.Spacer(length=bar.STRETCH),
                widget.Prompt(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.NvidiaSensors(format='{temp}°C'),
                widget.Battery(
                    format=fa.icons['microchip']+' {percent:2.0%} {hour:d}:{min:02d}',
                    # background='#03fc90',
                    charge_char='⚡',
                    decorations=[
                        RectDecoration(
                            colour="#f28fad",
                            radius=7,
                            filled=True,
                            padding_y=0,
                            padding_x=padding
                        ),
                    ]
                ),
                widget.Clock(
                    format=fa.icons["calendar"] + " %m/%d/%y %a",
                    decorations=[
                        RectDecoration(
                            colour="#38ffa9",
                            radius=7,
                            filled=True,
                            padding_y=0,
                            padding_x=padding
                        ),
                    ]),
                widget.Clock(
                    format=" %I:%M:%S %p",
                    # background="#03fcce", 
                    decorations = [
                        RectDecoration(
                            colour="#9debde",
                            radius=7,
                            filled=True,
                            padding_y=0,
                            padding_x=padding
                        ),
                    ]
                ),
                widget.PulseVolume(
                    decorations = [
                        RectDecoration(
                            colour="#ffffff",
                            radius=7,
                            filled=True,
                            padding_y=0,
                            padding_x=padding
                        ),
                    ],
                ),
            ],
            36,
            background="#000000.0",
            # background="#000000",
            opacity=1,
            border_width=0,
            # background="#ffffff", opacity=1
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
