# Desktop Entry

- 3 Types
  - `Application`: how to launch an application and what MIME types it supports (.desktop file extension)
  - `Link`: shortcut to a URL (.desktop file extension)
  - `Directory`: appearance of a submenu in the application menu (.directory file extension)

## Application

- Location:
  - `/usr/share/applications/` (system-wide)
  - `/usr/local/share/applications/` (system-wide deprecated)
  - `~/.local/share/applications/` (user-specific)
- To launch a .destkop file manually: `gtk-launch application.desktop`

```conf
[Desktop Entry]
Type=Application
Version=1.0
Name=Firefox
GenericName=Web Browser
GenericName[pt_BR]=Navegador Web
Comment=Browse the World Wide Web
Comment[pt_BR]=Navegue na Internet
Keywords=Internet;WWW;Browser;Web;Explorer
Keywords[pt_BR]=Internet;WWW;Browser;Web;Explorador;Navegador
Exec=env MOZ_ENABLE_WAYLAND=1 /usr/lib/firefox/firefox %u
Icon=firefox
Terminal=false
X-MultipleArgs=false
MimeType=text/html;text/xml;application/xhtml+xml;x-scheme-handler/http;x-scheme-handler/https;application/x-xpinstall;application/pdf;application/json;
StartupNotify=true
StartupWMClass=firefox
Categories=Network;WebBrowser;
Actions=new-window;new-private-window;

[Desktop Action new-window]
Name=New Window
Name[pt_PT]=Nova janela
Exec=env MOZ_ENABLE_WAYLAND=1 /usr/lib/firefox/firefox --new-window %u

[Desktop Action new-private-window]
Name=New Private Window
Name[pt_BR]=Nova janela privativa
Exec=env MOZ_ENABLE_WAYLAND=1 /usr/lib/firefox/firefox --private-window %u
```
