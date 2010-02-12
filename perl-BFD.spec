%define	upstream_name	 BFD
%define	upstream_version 0.31

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Impromptu dumping of data structures for debugging purposes  
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/R/RB/RBS/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:       noarch
BuildRoot:	 %{_tmppath}/%{name}-%{version}-%{release}

%description
Allows for impromptu dumping of output to STDERR. Useful when you want to take
a peek at a nest Perl data structure by emitting (relatively) nicely formatted
output with filename and line number prefixed to each line.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/BFD.pm
%{_mandir}/man3/*
