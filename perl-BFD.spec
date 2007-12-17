%define	module	BFD
%define	name	perl-%{module}
%define	version	0.31
%define	release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	 GPL or Artistic
Group:		 Development/Perl
Summary:         Impromptu dumping of data structures for debugging purposes  
Source0:         http://search.cpan.org/CPAN/authors/id/R/RB/RBS/%{module}-%{version}.tar.gz
Url:		 http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:       noarch

%description
Allows for impromptu dumping of output to STDERR. Useful when you want to take
a peek at a nest Perl data structure by emitting (relatively) nicely formatted
output with filename and line number prefixed to each line.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/BFD.pm
%{_mandir}/man3/*



