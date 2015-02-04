Name:           freedesktop-sdk
Version:        0.1
Release:        1%{?dist}
Summary:        Freedesktop sdk
Source1:        rpm-macros

License: Various
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

BuildRequires: freedesktop-platform
BuildRequires: freedesktop-sdk-base

Requires: freedesktop-platform
Requires: freedesktop-sdk-base

Requires: cairo-dev
Requires: cairo-gobject-dev
Requires: dbus-dev
Requires: desktop-file-utils
Requires: fontconfig-dev
Requires: freetype-dev
Requires: glib2-dev
Requires: gobject-introspection-dev
Requires: graphite2-dev
Requires: gstreamer1-dev
Requires: gtk-doc-stub
Requires: harfbuzz-dev
Requires: hunspell-dev
Requires: libICE-dev
Requires: libX11-dev
Requires: libXau-dev
Requires: libXcomposite-dev
Requires: libXcursor-dev
Requires: libXdamage-dev
Requires: libXdmcp-dev
Requires: libXext-dev
Requires: libXfixes-dev
Requires: libXft-dev
Requires: libXi-dev
Requires: libXinerama-dev
Requires: libXrandr-dev
Requires: libXrender-dev
Requires: libXt-dev
Requires: libXtst-dev
Requires: libXv-dev
Requires: libXxf86vm-dev
Requires: libepoxy-dev
Requires: libproxy-dev
Requires: libwayland-client-dev
Requires: libwayland-cursor-dev
Requires: libxcb-dev
Requires: libxkbcommon-dev
Requires: libxkbcommon-x11-dev
Requires: mesa-libEGL-dev
Requires: mesa-libGL-dev
Requires: mesa-libwayland-egl-dev
Requires: pixman-dev
Requires: pulseaudio-libs-dev
Requires: xkeyboard-config-dev
Requires: xorg-x11-util-macros

%description
Meta package for Gnome SDK dependencies

%prep


%build


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm/
install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros

%files
%doc
%{_sysconfdir}/rpm/macros

%changelog
* Fri Nov  7 2014 Alexander Larsson <alexl@redhat.com>
- Initial version