%define oversion 20120128

Summary:	An engine for 3D first-person shooter games Marathon 1, 2 and Infinity
Name:		AlephOne
Version:	1.0.1
Release:	2
License:	GPLv3+
Group:		Games/Arcade
Url:		http://sourceforge.net/projects/marathon/
Source0:	%{name}-%{oversion}.tar.bz2
Source1:	marathon.png
Patch0:		lua_templates.patch
BuildRequires:	boost-devel
BuildRequires:	smpeg-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(vorbisfile)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(zziplib)
Provides:	alephone = %{EVRD}

%description
Aleph One is an engine to run Marathon, Marathon 2 and Marathon Infinity games.

Packages with game data are:
- marathon
- marathon2
- marathon-infinity

%files
%doc AUTHORS COPYING README docs/MML.html
%{_gamesbindir}/alephone
%{_gamesdatadir}/%{name}
%{_datadir}/pixmaps/marathon.png
%{_mandir}/man6/*.6*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{oversion}
%patch0 -p0 $startdir/lua_templates.patch Source_Files/Lua/lua_templates.h

%build
%configure2_5x	\
	--bindir=%{_gamesbindir} \
	--datadir=%{_gamesdatadir} \
	--enable-opengl
%make

%install
%makeinstall_std
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/

