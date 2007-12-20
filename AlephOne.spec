%define name	AlephOne
%define version 0.13.0
%define release %mkrel 0.20051119.4

Summary:	3D first-person shooter game
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Arcade
Source0:	%name-20051119.tar.bz2
Source1:	%{name}-icons.tar.bz2
Patch0:         AlephOne-fix-build.patch 
URL:		http://sourceforge.net/projects/marathon/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: libSDL-devel
BuildRequires: libMesaGLU-devel
BuildRequires: SDL_net-devel
BuildRequires: boost-devel


%description
Aleph One is an Open Source 3D first-person shooter game, based on the game
Marathon 2 by Bungie Software. It supports OpenGL, but doesn't require, for
rendering.

This package requires additional data -- shape, sound, and map information
-- in order to be installed. One source of this core data is the
AlephOne-minf-demo package.

%prep

%setup -q -n %name-20051119
%patch0 -p1
%build
export LDFLAGS="-L%_prefix/X11R6/%_lib $LDFLAGS"

%configure	--bindir=%_gamesbindir \
		--datadir=%_datadir/games \
		--enable-opengl
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application <<EOF
Exec=%_gamesbindir/alephone
Name=Alephone
Comment=First person shooter game
Icon=%{name}
Categories=Game;ArcadeGame;
EOF

install -d ${RPM_BUILD_ROOT}{%{_miconsdir},%{_liconsdir}}
tar -xOjf %{SOURCE1} icons/16x16.png > ${RPM_BUILD_ROOT}%{_miconsdir}/%{name}.png
tar -xOjf %{SOURCE1} icons/32x32.png > ${RPM_BUILD_ROOT}%{_iconsdir}/%{name}.png
tar -xOjf %{SOURCE1} icons/48x48.png > ${RPM_BUILD_ROOT}%{_liconsdir}/%{name}.png

rm -fr $RPM_BUILD_ROOT/%_bindir/
rm -fr $RPM_BUILD_ROOT/%_datadir/%name

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL.Unix README docs/MML.html docs/Cheat_Codes
%{_gamesbindir}/alephone
%{_datadir}/games/%{name}/Fonts
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/MML
%{_datadir}/games/%{name}/MML/*.mml
%dir %{_datadir}/games/%{name}/Themes
%dir %{_datadir}/games/%{name}/Themes/Default
%{_datadir}/games/%{name}/Themes/Default/*.bmp
%{_datadir}/games/%{name}/Themes/Default/resources
%{_datadir}/games/%{name}/Themes/Default/theme.mml
%{_datadir}/applications/mandriva-*.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


