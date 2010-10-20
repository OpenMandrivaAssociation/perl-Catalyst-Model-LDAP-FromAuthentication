%define upstream_name    Catalyst-Model-LDAP-FromAuthentication
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Provides an LDAP model bound as the user who logged in
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
# Get 0.01, which is not on CPAN, at:
# http://github.com/bobtfish/catalyst-model-ldap-fromauthentication/tarball/0.01
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Catalyst::Authentication::Store::LDAP)
BuildRequires: perl(Catalyst::Component::InstancePerContext)
BuildRequires: perl(Catalyst::Model::LDAP)
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Types::Common::String)
#BuildRequires: perl(MooseX::Types::LoadableClass)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(Module::Install)
BuildRequires: perl(Module::CoreList)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
perl -pi -e 's/^(use Module::Install::Author)/#$1/g;s/^(author_)/#$1/g' Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


