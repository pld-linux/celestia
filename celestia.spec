Summary:	A real-time visual space simulation
Summary(pl):	Symulacja przestrzeni kosmicznej w czasie rzeczywistym
Name:		celestia
Version:	1.1.4
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://prdownloads.sourceforge.net/celestia/%{name}-%{version}.tar.gz
URL:		http://www.shatters.net/celestia/
BuildRequires:	libpng-devel libjpeg-devel glut-devel OpenGL-devel gtk+-devel gtkglarea-devel 
BuildRequires:	/usr/share/automake/depcomp
Requires:	libpng libjpeg glut OpenGL gtk+ gtkglarea 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _noautoreqdep   libGL.so.1 libGLU.so.1 libGLcore.so.1
%define         _noreqdep  	 libGL.so.1 libGLU.so.1 libGLcore.so.1
%define		_prefix		/usr/X11R6
%define		_datadir	%{_prefix}/share
%define		_mandir		%{_prefix}/man

%description
Celestia is a free real-time space simulation that lets you experience
our universe in three dimensions. Unlike most planetarium software,
Celestia doesn't confine you to the surface of the Earth. You can
travel throughout the solar system, to any of over 100,000 stars, or
even beyond the galaxy. All travel in Celestia is seamless; the
exponential zoom feature lets you explore space across a huge range of
scales, from galaxy clusters down to spacecraft only a few meters
across. A 'point-and-goto' interface makes it simple to navigate
through the universe to the object you want to visit.

%description -l pl
Celestia to wolny symulator przestrzeni komicznej w czasie
rzeczywistym, który pozwala do¶wiadczaæ naszego Wszech¶wiata w trzech
wymiarach. W odró¿nieniu od innych programów planetarnych Celestia nie
przywi±zuje Ciê do powierzchni ziemi. Mo¿esz podró¿owaæ przez Uk³ad
S³oneczny do ponad 100,000 gwiazd lub nawet poza galaktykê. Wszystkie
podró¿e w Celestii s± niezauwa¿alne; funkcja wyk³adniczego
przybli¿enia pozwala Ci odkrywaæ Kosmos w ró¿nych skalach - od
spojrzenia na galaktyki do widoku kilkumetrowych statków kosmicznych.
Interfejs typu 'poka¿-i-leæ' czyni nawigacjê przez Wszech¶wiat prost±.

%prep
%setup -q
# This is some kind of problem with automake:
ln -s /usr/share/automake/depcomp

%build
export CC=%{__cc}
./configure --prefix=%{_prefix} --enable-gtk
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -e DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README AUTHORS TODO controls.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz AUTHOR.gz TODO.gz controls.txt.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/*
