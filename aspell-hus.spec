Summary:	Huastec dictionary for aspell
Summary(pl.UTF-8):	Słownik języka wastek dla aspella
Name:		aspell-hus
Version:	0.03
%define	subv	1
Release:	3
License:	GPL v3+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/hus/aspell6-hus-%{version}-%{subv}.tar.bz2
# Source0-md5:	0414c746826b4f9d7e606ca60c44f102
URL:		http://aspell.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Huastec dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik (lista słów) języka wastek dla aspella.

%prep
%setup -q -n aspell6-hus-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_prefix}/lib/aspell/hus.multi
%{_prefix}/lib/aspell/hus.rws
%{_datadir}/aspell/hus.dat
%{_datadir}/aspell/hus_affix.dat
