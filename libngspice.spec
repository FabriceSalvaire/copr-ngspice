Name:               libngspice
Version:            27
Release:            1%{?dist}
Summary:            A mixed level/signal circuit simulator
License:            BSD
URL:                http://ngspice.sourceforge.net

Source0:            https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%{version}/ngspice-%{version}.tar.gz
# Source1:          https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%{version}/ngspice-%{version}-manual.pdf

BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:      readline-devel
BuildRequires:      automake
BuildRequires:      libtool
BuildRequires:      bison
BuildRequires:      byacc
BuildRequires:      flex

# Requires:

#---------------------------------------------------------------------------------------------------

%description
Ngspice is a mixed-level/mixed-signal circuit simulator, based on
three open source software packages: Spice3f5, Cider1b1 and Xspice.

This package provides the libngspice.so library.

#---------------------------------------------------------------------------------------------------

# Command or series of commands to prepare the software to be built.
%prep
%autosetup -n ngspice-%{version}

export ACLOCAL_FLAGS=-Im4
./autogen.sh # --adms

#---------------------------------------------------------------------------------------------------

%build

export CFLAGS="%{optflags}" # else configure fails

%configure \
  --enable-cider \
  --enable-openmp \
  --enable-xspice \
  --with-ngshared \
  --with-readline=yes \
  %{nil}

# --disable-debug \
# --enable-maintainer-mode \
# --enable-dependency-tracking \

%make_build

#---------------------------------------------------------------------------------------------------

%install
rm -rf $RPM_BUILD_ROOT
%make_install

#---------------------------------------------------------------------------------------------------

%clean
rm -rf $RPM_BUILD_ROOT

#---------------------------------------------------------------------------------------------------

%files
%{_bindir}/*
%{_includedir}/ngspice/*
%{_libdir}/libngspice*
%{_libdir}/ngspice/
%{_mandir}/man1/*
%{_datadir}/ngspice/*
%license COPYING

#---------------------------------------------------------------------------------------------------

%changelog
* Sun Sep 17 2017 Fabrice Salvaire <pyspice [AT] fabrice-salvaire DOT fr>
- Initial Package for Fedora Copr
