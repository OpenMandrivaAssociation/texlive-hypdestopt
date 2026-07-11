%global tl_name hypdestopt
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.9
Release:	%{tl_revision}.1
Summary:	Hyperref destination optimizer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hypdestopt
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdestopt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hypdestopt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package supports hyperref's pdfTeX driver. It removes unnecessary
destinations and shortens the destination names or uses numbered
destinations to get smaller PDF files.

