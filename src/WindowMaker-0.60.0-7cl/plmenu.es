(
"GNU WindowMaker",
	(
	"Info",
		("Info Panel...", INFO_PANEL),
		("Legal", LEGAL_PANEL),
		(
		"Consola del Sistema",
		EXEC,
		"xconsole"
		),
		(
		"Carga del Sistema",
		EXEC,
		"xosview || xload"
		),
		(
		"Lista de Procesos",
		EXEC,
		"xterm -e top"
		),
		(
		"Manual de usuario",
		EXEC,
		"xman"
		)
	),
	(
	"XTerm",
	EXEC,
	"xterm -sb"
	),
    (
    "Programas",
    OPEN_MENU,
    "| wmconfig --output wmaker --no-promote 2>/dev/null"
    ),
	("Escritorios", WORKSPACE_MENU),
	(
	"Selección",
		(
		"Copiar",
		EXEC,
		"echo '%s' | wxcopy"
		),
		(
		"Enviar a",
		EXEC,
		"xterm -name mail -T \"Pine\" -e pine %s"
		),
		(
		"Navigar",
		EXEC,
		"netscape %s"
		),
		(
		"Buscar en el Manual",
		EXEC,
		"if ( man  %s  > /dev/null ); then man  %s  | xless;	else xmessage -center -title \"Manual Browser\" Sorry, but there is no manual page entry for  %s ...; fi"
		)
	),
	(
	"Escritorio",
		("Ocultar otras", HIDE_OTHERS),
		("Mostrar todas", SHOW_ALL),
		("Arreglar Iconos", ARRANGE_ICONS),
		("Refrescar", REFRESH),
		(
		"Bloquear",
		EXEC,
		"xlock -allowroot -usefirst"
		),
		("Guardar Sesión", SAVE_SESSION),
		("Borrar Sesión Guardada", CLEAR_SESSION)
	),
	(
	"Apariencia",
		(
		"Temas",
		OPEN_MENU,
		"-noext  /usr/X11R6/share/WindowMaker/Themes  $HOME/GNUstep/Library/WindowMaker/Themes WITH setstyle"
		),
		(
		"Estilos",
		OPEN_MENU,
		"-noext  /usr/X11R6/share/WindowMaker/Styles  $HOME/GNUstep/Library/WindowMaker/Styles WITH setstyle"
		),
		(
		"Juegos de Iconos",
		OPEN_MENU,
		"-noext  /usr/X11R6/share/WindowMaker/IconSets  $HOME/GNUstep/Library/WindowMaker/IconSets WITH seticons"
		),
		(
		"Fondo",
			(
			"Sólido",
                        	(
                        	"Black",
                        	EXEC,
                        	"wdwrite WindowMaker WorkspaceBack  '(solid, black)'"
                        	),
                        	(
                        	"Blue",
                        	EXEC,
                        	"wdwrite WindowMaker WorkspaceBack  '(solid, \"#505075\")'"
                        	),
				(
				"Indigo",
				EXEC,
				"wdwrite WindowMaker WorkspaceBack  '(solid, \"#243e6c\")'"
				),
				(
				"Deep Blue",
				EXEC,
				"wdwrite WindowMaker WorkspaceBack  '(solid, \"#180090\")'"
				),
                        	(
                        	"Purple",
                        	EXEC,
                        	"wdwrite WindowMaker WorkspaceBack  '(solid, \"#554466\")'"
                        	),
                        	(
                        	"Wheat",
                        	EXEC,
                        	"wdwrite WindowMaker WorkspaceBack  '(solid, \"wheat4\")'"
                        	),
                        	(
                        	"Dark Gray",
                        	EXEC,
                        	"wdwrite WindowMaker WorkspaceBack  '(solid, \"#333340\")'"
                        	),
                        	(
                        	"Wine",
                        	EXEC,
                        	"wdwrite WindowMaker WorkspaceBack  '(solid, \"#400020\")'"
                        	)
			),
			(
			"Gradiente",
				(
				"Flag",
				EXEC,
				"wdwrite WindowMaker WorkspaceBack  '(mdgradient, green, red, white, green)'"
				),
				(
				"Sky",
				EXEC,
				"wdwrite WindowMaker WorkspaceBack  '(vgradient, blue4, white)'"
				)
			),
			(
			"Imagenes",
			OPEN_MENU,
			"-noext  /usr/X11R6/share/WindowMaker/Backgrounds  $HOME/GNUstep/Library/WindowMaker/Backgrounds WITH wmsetbg -u -t"
			)
		),
		(
		"Guardar Tema",
		EXEC,
		"getstyle -t $HOME/GNUstep/Library/WindowMaker/Themes/\"%a(Theme name)\""
		),
		(
		"Guardar Juego de Iconos",
		EXEC,
		"geticonset $HOME/GNUstep/Library/WindowMaker/IconSets/\"%a(IconSet name)\""
		)
	),
	(
	"Salir",
        ("Rearrancar", RESTART),
        (
        "Alternar para...",
            ("AfterStep", RESTART, /usr/X11R6/bin/RunWM.AfterStep),
            ("Fvwm2 (Fvwm95)", RESTART, /usr/X11R6/bin/RunWM.Fvwm95),
            ("Fvwm2 (MWM)", RESTART, /usr/X11R6/bin/RunWM.MWM),
            ("icewm", RESTART, /usr/X11R6/bin/RunWM.icewm)
        ),
        ("Salir...", EXIT),
        ("Cerrar la sesión...", SHUTDOWN)
	)
)
