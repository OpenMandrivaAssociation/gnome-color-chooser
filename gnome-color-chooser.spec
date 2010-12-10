Name:		gnome-color-chooser
Summary:	Customize the appearance of the GNOME desktop
Version: 	0.2.5
Release:	%mkrel 2
License: 	GPLv3+
Group:		Graphical desktop/GNOME
Source0:	%{name}/%{name}-%{version}.tar.bz2
Patch:		gnome-color-chooser-0.2.5-desktop-entry.patch
URL: 		http://sourceforge.net/projects/gnomecc
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:  libgnomeuimm2.6-devel
BuildRequires:  intltool


%description
An application for customizing the appearance of the GNOME(/GTK+) desktop.
Features: change colors and sizes of GTK widgets, colorize desktop
icons, configure your gtk engines and let your current theme be
drawn by whatever gtk engine you want, etc.


%prep

%setup -q
%patch -p1

%build

%configure2_5x
%make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %name


%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-, root, root)
%doc README THANKS NEWS AUTHORS
%_bindir/%name
%_datadir/applications/%name.desktop
%dir %_datadir/%name/
%_datadir/%name/glade/%name.glade
%_datadir/%name/profiles/compact.xml
%_datadir/%name/%name.xml
%_datadir/man/man1/%name.1*
%_datadir/pixmaps/%name.svg

