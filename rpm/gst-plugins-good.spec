%define majorminor  1.0
%define gstreamer   gstreamer

Name: 		%{gstreamer}%{majorminor}-plugins-good
Version: 	1.18.1
Release: 	1
Summary: 	GStreamer plug-ins with good code and licensing
License: 	LGPLv2+
URL:		http://gstreamer.freedesktop.org/
Source:         http://gstreamer.freedesktop.org/src/gst-plugins-good/gstreamer1.0-plugins-good-%{version}.tar.xz
Patch0:         0001-Set-specific-media.role-for-pulsesink-probe.patch
Patch1:         0002-qtmux-write-rotation-information-into-the-TKHD-matri.patch

%define sonamever %(echo %{version} | cut -d '+' -f 1)

Requires:      gstreamer1.0
Requires:      orc >= 0.4.18
BuildRequires: pkgconfig(flac)
BuildRequires: libjpeg-devel
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(speex)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(vpx)
BuildRequires: pkgconfig(libmpg123)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0) >= %{sonamever}
BuildRequires: pkgconfig(orc-0.4) >= 0.4.18
BuildRequires: bzip2-devel
BuildRequires: meson
BuildRequires: libtool
BuildRequires: gettext-devel

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

%prep
%autosetup -p1 -n gstreamer1.0-plugins-good-%{version}/gst-plugins-good

%build
%meson \
  -Dpackage-name='SailfishOS GStreamer package plugins (good set)' \
  -Dpackage-origin='http://sailfishos.org/' \
  -Dnls=disabled \
  -Ddoc=disabled \
  -Dexamples=disabled \
  -Dorc=enabled \
  -Dvpx=enabled \
  -Dv4l2-probe=false \
  -Dv4l2-libv4l2=disabled \
  -Doss=disabled -Doss4=disabled \
  -Dy4m=disabled \
  -Dtaglib=disabled \
  -Dqt5=disabled \
  -Dximagesrc=disabled \
  -Daalib=disabled \
  -Dgdk-pixbuf=disabled -Dgtk3=disabled \
  -Djack=disabled \
  -Dlame=disabled -Dtwolame=disabled \
  -Dlibcaca=disabled \
  -Ddv=disabled \
  -Ddv1394=disabled \
  -Dshout2=disabled \
  -Dwavpack=disabled \
  -Dmonoscope=disabled \
  -Drpicamsrc=disabled

%meson_build

%install
%meson_install

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -fr $RPM_BUILD_ROOT%{_mandir}

%files
%defattr(-, root, root)
%license COPYING
%dir %{_datadir}/gstreamer-%{majorminor}/presets
%{_datadir}/gstreamer-%{majorminor}/presets/GstIirEqualizer10Bands.prs
%{_datadir}/gstreamer-%{majorminor}/presets/GstIirEqualizer3Bands.prs
%{_datadir}/gstreamer-%{majorminor}/presets/GstQTMux.prs
%{_datadir}/gstreamer-%{majorminor}/presets/GstVP8Enc.prs
%{_libdir}/gstreamer-%{majorminor}/libgstalaw.so
%{_libdir}/gstreamer-%{majorminor}/libgstalphacolor.so
%{_libdir}/gstreamer-%{majorminor}/libgstalpha.so
%{_libdir}/gstreamer-%{majorminor}/libgstapetag.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudiofx.so
%{_libdir}/gstreamer-%{majorminor}/libgstaudioparsers.so
%{_libdir}/gstreamer-%{majorminor}/libgstauparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstautodetect.so
%{_libdir}/gstreamer-%{majorminor}/libgstavi.so
%{_libdir}/gstreamer-%{majorminor}/libgstcairo.so
%{_libdir}/gstreamer-%{majorminor}/libgstcutter.so
%{_libdir}/gstreamer-%{majorminor}/libgstdebug.so
%{_libdir}/gstreamer-%{majorminor}/libgstdeinterlace.so
%{_libdir}/gstreamer-%{majorminor}/libgstdtmf.so
%{_libdir}/gstreamer-%{majorminor}/libgsteffectv.so
%{_libdir}/gstreamer-%{majorminor}/libgstequalizer.so
%{_libdir}/gstreamer-%{majorminor}/libgstflac.so
%{_libdir}/gstreamer-%{majorminor}/libgstflv.so
%{_libdir}/gstreamer-%{majorminor}/libgstflxdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstgoom2k1.so
%{_libdir}/gstreamer-%{majorminor}/libgstgoom.so
%{_libdir}/gstreamer-%{majorminor}/libgsticydemux.so
%{_libdir}/gstreamer-%{majorminor}/libgstid3demux.so
%{_libdir}/gstreamer-%{majorminor}/libgstimagefreeze.so
%{_libdir}/gstreamer-%{majorminor}/libgstinterleave.so
%{_libdir}/gstreamer-%{majorminor}/libgstisomp4.so
%{_libdir}/gstreamer-%{majorminor}/libgstjpeg.so
%{_libdir}/gstreamer-%{majorminor}/libgstlevel.so
%{_libdir}/gstreamer-%{majorminor}/libgstmatroska.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpg123.so
%{_libdir}/gstreamer-%{majorminor}/libgstmulaw.so
%{_libdir}/gstreamer-%{majorminor}/libgstmultifile.so
%{_libdir}/gstreamer-%{majorminor}/libgstmultipart.so
%{_libdir}/gstreamer-%{majorminor}/libgstnavigationtest.so
%{_libdir}/gstreamer-%{majorminor}/libgstpng.so
%{_libdir}/gstreamer-%{majorminor}/libgstpulseaudio.so
%{_libdir}/gstreamer-%{majorminor}/libgstreplaygain.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtpmanager.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtp.so
%{_libdir}/gstreamer-%{majorminor}/libgstrtsp.so
%{_libdir}/gstreamer-%{majorminor}/libgstshapewipe.so
%{_libdir}/gstreamer-%{majorminor}/libgstsmpte.so
%{_libdir}/gstreamer-%{majorminor}/libgstsoup.so
%{_libdir}/gstreamer-%{majorminor}/libgstspectrum.so
%{_libdir}/gstreamer-%{majorminor}/libgstspeex.so
%{_libdir}/gstreamer-%{majorminor}/libgstudp.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideo4linux2.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideobox.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideocrop.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideofilter.so
%{_libdir}/gstreamer-%{majorminor}/libgstvideomixer.so
%{_libdir}/gstreamer-%{majorminor}/libgstvpx.so
%{_libdir}/gstreamer-%{majorminor}/libgstwavenc.so
%{_libdir}/gstreamer-%{majorminor}/libgstwavparse.so
