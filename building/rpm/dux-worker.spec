Name:       dux-worker
Version:    PLACEHOLDER_FOR_VERSION
Release:    0
Summary:    Automation tool written in Rust
License:    Apache License, Version 2.0
URL:        https://gitlab.com/dux-tool/dux
Packager:   romzorus <romzorus591@gmail.com>


%description
A scalable and cloud-friendly automation / orchestration tool (worker component) written in Rust.

%install
mkdir -p %{buildroot}/usr/bin
cp dux-worker %{buildroot}/usr/bin/
mkdir -p %{buildroot}/etc/dux-worker
cp dux-worker.conf %{buildroot}/etc/dux-worker/

%files
/usr/bin/dux-worker
/etc/dux-worker/dux-worker.conf
