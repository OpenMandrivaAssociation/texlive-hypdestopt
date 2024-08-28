Name:		texlive-hypdestopt
Version:	71991
Release:	1
Summary:	Hyperref destination optimizer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hypdestopt
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdestopt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdestopt.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package supports hyperref's pdfTeX driver. It removes
unnecessary destinations and shortens the destination names or
uses numbered destinations to get smaller PDF files.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/hypdestopt
%doc %{_texmfdistdir}/doc/latex/hypdestopt

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
