# Generated from flexmock-0.9.0.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	flexmock

Summary:	Simple and Flexible Mock Objects for Testing
Name:		rubygem-%{rbname}

Version:	0.9.0
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://github.com/jimweirich/flexmock
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
FlexMock is a extremely simple mock object class compatible
with the Test::Unit framework.  Although the FlexMock's
interface is simple, it is very flexible.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f test

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/flexmock
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/flexmock/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/flexmock/rails
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/flexmock/rails/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test/rspec_integration
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/rspec_integration/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test/test_unit_integration
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/test_unit_integration/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%{ruby_gemdir}/gems/%{rbname}-%{version}/CHANGES
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/doc
%{ruby_gemdir}/gems/%{rbname}-%{version}/doc/*.rdoc
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/doc/releases
%{ruby_gemdir}/gems/%{rbname}-%{version}/doc/releases/*.rdoc
