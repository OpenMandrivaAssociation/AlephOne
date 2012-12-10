%define		oversion	20120128
#define debug_package %{nil}
Name:		AlephOne
Version:		1.0.1
Release:		1
Summary:		An engine for 3D first-person shooter games Marathon 1, 2 and Infinity
License:		GPL
Group:		Games/Arcade
Source0:		%{name}-%{oversion}.tar.bz2
Source1:		marathon.png
Patch0:		lua_templates.patch
URL:		http://sourceforge.net/projects/marathon/
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(vorbisfile)
BuildRequires:	boost-devel
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	png-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	smpeg-devel
BuildRequires:	zlib-devel
BuildRequires:	zziplib-devel
Provides:	alephone = %{version}-%{release}

%description
Aleph One is an engine to run Marathon, Marathon 2 and Marathon Infinity games.

Packages with game data are:
- marathon
- marathon2
- marathon-infinity

%prep
%setup -q -n %{name}-%{oversion}
%patch0 -p0 $startdir/lua_templates.patch Source_Files/Lua/lua_templates.h



%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir} \
		--enable-opengl
%make

%install
%makeinstall_std
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__cp %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/


%files
%doc AUTHORS COPYING README docs/MML.html
%{_gamesbindir}/alephone
%{_gamesdatadir}/%{name}
%{_datadir}/pixmaps/marathon.png
%{_mandir}/man6/*.6.*

