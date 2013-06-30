#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Math
%define		pnam	Complex
%include	/usr/lib/rpm/macros.perl
Summary:	Math::Complex - complex numbers and associated mathematical functions
Summary(pl.UTF-8):	Math::Complex - liczby zespolone i związane z nimi funkcje matematyczne
Name:		perl-Math-Complex
Version:	1.59
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94f9d6b557b56408949928a55227c86f
URL:		http://search.cpan.org/dist/Math-Complex/
BuildRequires:	perl-Scalar-List-Utils >= 1.11
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package lets you create and manipulate complex numbers. By
default, Perl limits itself to real numbers, but an extra use
statement brings full complex support, along with a full set of
mathematical functions typically associated with and/or extended to
complex numbers.

%description -l pl.UTF-8
Ten pakiet pozwala na tworzenie i operowanie na liczbach zespolonych.
Domyślnie Perl jest ograniczony do samych liczb rzeczywistych, ale
dodatkowa instrukcja "use" zapewnia obsługę liczb zespolonych, wraz ze
zbiorem funkcji matematycznych typowo związanych z liczbami
zespolonymi lub rozszerzonych o obsługę liczb zespolonych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO
%{perl_vendorlib}/Math/Complex.pm
%{perl_vendorlib}/Math/Trig.pm
%{_mandir}/man3/Math::Complex.3pm*
%{_mandir}/man3/Math::Trig.3pm*
