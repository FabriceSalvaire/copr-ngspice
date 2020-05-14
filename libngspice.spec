# Doc http://rpm.org/documentation.html
# https://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/RPM_Guide/ch-specfiles.html

Name:               libngspice
Version:            32
Release:            1%{?dist}
Summary:            A mixed level/signal circuit simulator
License:            BSD
URL:                http://ngspice.sourceforge.net

Source0:            https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%{version}/ngspice-%{version}.tar.gz

BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gcc

# BuildRequires:    readline-devel
BuildRequires:      automake
BuildRequires:      libtool
BuildRequires:      bison
BuildRequires:      byacc
BuildRequires:      flex

# BuildRequires:	git

# Requires:

#---------------------------------------------------------------------------------------------------

%description
Ngspice is a mixed-level/mixed-signal circuit simulator, based on
three open source software packages: Spice3f5, Cider1b1 and Xspice.

This package provides the libngspice.so library compiled using:

  --enable-openmp
  --enable-cider
  --enable-xspice

#---------------------------------------------------------------------------------------------------

# Command or series of commands to prepare the software to be built.
%prep
%setup -q -n ngspice-%{version}
# The -n option is used to set the name of the software's build directory.
#   This is necessary only when the source archive unpacks into a directory named other than <name>- <version>.
# The -q option is used to direct %setup to quiet its output.
#   Verbose file listings won't be displayed when unpacking archives with this option.
# autosetup -n ngspice-%{version}

export ACLOCAL_FLAGS=-Im4
./autogen.sh # --adms

#---------------------------------------------------------------------------------------------------

%build

export CFLAGS="%{optflags}" # else configure fails

# --disable-debug #  No debugging information included (optimized and compact code)
# --enable-cider  # Include CIDER numerical device simulator
# --enable-openmp # Compile ngspice for multi-core processors. Paralleling is done by OpenMP (see Chapt. 16.10), and is enabled for certain MOS models.
# --enable-xspice # Include the XSPICE extensions

# --with-readline=yes \

# ???
# --disable-silent-rules \
# --enable-adms \
# --enable-dependency-tracking \
# --enable-maintainer-mode \
# --enable-predictor \

%configure \
  --disable-debug \
  --enable-cider \
  --enable-openmp \
  --enable-xspice \
  --with-ngshared \
  %{nil}

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
%{_datadir}/ngspice/*
%{_includedir}/ngspice/*
%{_libdir}/libngspice*
%{_libdir}/ngspice/
%{_libdir}/pkgconfig/ngspice.pc
%{_mandir}/man1/*
%license COPYING

#---------------------------------------------------------------------------------------------------

%changelog
* Thu May 14 2020 Fabrice Salvaire <pyspice [AT] fabrice-salvaire DOT fr>
- v32
* Sun Sep 17 2017 Fabrice Salvaire <pyspice [AT] fabrice-salvaire DOT fr>
- Initial Package for Fedora Copr
