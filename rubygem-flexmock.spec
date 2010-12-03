%define oname flexmock

Name:       rubygem-%{oname}
Version:    0.8.11
Release:    %mkrel 1
Summary:    Simple and Flexible Mock Objects for Testing
Group:      Development/Ruby
License:    MIT
URL:        http://flexmock.rubyforge.org
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
FlexMock is a extremely simple mock object class compatible
with the Test::Unit framework.  Although the FlexMock's
interface is simple, it is very flexible.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/ \
  -type f -exec sed -i -e "/^#!/d" {} \; -exec chmod -x {} \;

find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/test/ \
  -type f -exec chmod +x {} \;

find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/doc/ \
  -name "*.rdoc" -exec chmod -x {} \;
%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/flexmock.blurb
%{ruby_gemdir}/gems/%{oname}-%{version}/install.rb
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGES
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/doc/
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
