%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

%define _includedir %{_prefix}/include/SDL

Summary:	Simple DirectMedia Layer for pango
Name:		SDL_Pango
Version:	0.1.2
Release:	22
License:	LGPLv2+
Group:		System/Libraries
Url:		http://sdlpango.sourceforge.net/
Source0:	http://puzzle.dl.sourceforge.net/sourceforge/sdlpango/%{name}-%{version}.tar.bz2
Patch0:		SDL_Pango-0.1.2-API-adds.patch
Patch1:		sdl_pango_fix_build_clang.patch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangoft2)

%description
Pango is the text rendering engine of GNOME.
SDL_Pango connects the engine to SDL.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%apply_patches

libtoolize --force
aclocal -I m4
automake -a
autoconf

%build
%configure --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libSDL_Pango.so.%{major}*

%files -n %{devname}
%doc README
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
