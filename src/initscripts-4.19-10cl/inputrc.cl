# Conectiva Linux - JUN/1999
# Com várias seqüências de teclas compiladas por Carlos A. M. dos Santos,
# mantenedor do Portuguese-HOWTO
#
# /etc/inputrc
#

# Aceita caracteres com 8 bits
set meta-flag on
set convert-meta off
set output-meta on

# Se quiser modo vi
# set editing-mode vi

# emacs é o modo padrão
$if mode=emacs
  # Configuração para diversos terminais
  $if term=sun
     "\C-?":delete-char
  $endif
  $if term=vt100
     "\C-?":delete-char
  $endif
  $if term=xterm
     "\C-?":delete-char
  $endif
  $if term=xterm-color
     "\C-?":delete-char
  $endif
  $if term=sun-cmd
     "\C-?":backward-delete-char
  $endif
  
  # Seqüências ANSI
  "\e[1~":beginning-of-line
  "\e[3~":delete-char
  "\e[4~":end-of-line
  "\e[5~":beginning-of-history
  "\e[6~":end-of-history
  "\e[7~":beginning-of-line
  "\e[8~":end-of-line
  "\e[A":previous-history
  "\e[B":next-history
  "\e[C":forward-char
  "\e[D":backward-char
  
  # XTerm
  "\e[\C-@":beginning-of-line
  "\e[E":beginning-of-line
  "\e[H":beginning-of-line
  "\eOH":beginning-of-line
  "\e[F":end-of-line
  "\eOF":end-of-line
  "\e[e":end-of-line
  
  # Console Sun (testado com teclados Type 4/5)
  # "\e[247z": Ainda não encontrei uso para a tecla INSERT...
  "\e[214z":beginning-of-line
  "\e[220z":end-of-line
  "\e[216z":beginning-of-history
  "\e[222z":end-of-history
  "\e[249z":delete-char
  
  # xiterm (AfterStep)
  "\e0d": backward-word
  "\e0c": forward-word

  # rxvt
  "\eOc": forward-word
  "\eOd": backward-word
  
  # outros
  "\e[h": beginning-of-line
  "\e[f": end-of-line
  "\e[d": backward-word
  "\e[c": forward-word
$endif

$if Bash
  # Editar o PATH com "ctrl-x p"
  "\C-xp": "PATH=${PATH}\e\C-e\C-a\ef\C-f"
$endif
