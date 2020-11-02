#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : msgpack-c
Version  : 3.2.0
Release  : 3
URL      : https://github.com/msgpack/msgpack-c/archive/cpp-3.2.0.tar.gz
Source0  : https://github.com/msgpack/msgpack-c/archive/cpp-3.2.0.tar.gz
Summary  : Binary-based efficient object serialization library
Group    : Development/Tools
License  : BSL-1.0
Requires: msgpack-c-lib = %{version}-%{release}
Requires: msgpack-c-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : zlib-dev

%description
`msgpack` for C/C++
===================
Version 3.2.0 [![Build Status](https://travis-ci.org/msgpack/msgpack-c.svg?branch=master)](https://travis-ci.org/msgpack/msgpack-c) [![Build status](https://ci.appveyor.com/api/projects/status/8kstcgt79qj123mw/branch/master?svg=true)](https://ci.appveyor.com/project/redboltz/msgpack-c/branch/master)

%package dev
Summary: dev components for the msgpack-c package.
Group: Development
Requires: msgpack-c-lib = %{version}-%{release}
Provides: msgpack-c-devel = %{version}-%{release}
Requires: msgpack-c = %{version}-%{release}

%description dev
dev components for the msgpack-c package.


%package lib
Summary: lib components for the msgpack-c package.
Group: Libraries
Requires: msgpack-c-license = %{version}-%{release}

%description lib
lib components for the msgpack-c package.


%package license
Summary: license components for the msgpack-c package.
Group: Default

%description license
license components for the msgpack-c package.


%prep
%setup -q -n msgpack-c-cpp-3.2.0
cd %{_builddir}/msgpack-c-cpp-3.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604359911
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1604359911
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/msgpack-c
cp %{_builddir}/msgpack-c-cpp-3.2.0/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/msgpack-c/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/msgpack.h
/usr/include/msgpack.hpp
/usr/include/msgpack/adaptor/adaptor_base.hpp
/usr/include/msgpack/adaptor/adaptor_base_decl.hpp
/usr/include/msgpack/adaptor/array_ref.hpp
/usr/include/msgpack/adaptor/array_ref_decl.hpp
/usr/include/msgpack/adaptor/bool.hpp
/usr/include/msgpack/adaptor/boost/fusion.hpp
/usr/include/msgpack/adaptor/boost/msgpack_variant.hpp
/usr/include/msgpack/adaptor/boost/msgpack_variant_decl.hpp
/usr/include/msgpack/adaptor/boost/optional.hpp
/usr/include/msgpack/adaptor/boost/string_ref.hpp
/usr/include/msgpack/adaptor/boost/string_view.hpp
/usr/include/msgpack/adaptor/carray.hpp
/usr/include/msgpack/adaptor/char_ptr.hpp
/usr/include/msgpack/adaptor/check_container_size.hpp
/usr/include/msgpack/adaptor/check_container_size_decl.hpp
/usr/include/msgpack/adaptor/cpp11/array.hpp
/usr/include/msgpack/adaptor/cpp11/array_char.hpp
/usr/include/msgpack/adaptor/cpp11/array_unsigned_char.hpp
/usr/include/msgpack/adaptor/cpp11/chrono.hpp
/usr/include/msgpack/adaptor/cpp11/forward_list.hpp
/usr/include/msgpack/adaptor/cpp11/reference_wrapper.hpp
/usr/include/msgpack/adaptor/cpp11/shared_ptr.hpp
/usr/include/msgpack/adaptor/cpp11/timespec.hpp
/usr/include/msgpack/adaptor/cpp11/tuple.hpp
/usr/include/msgpack/adaptor/cpp11/unique_ptr.hpp
/usr/include/msgpack/adaptor/cpp11/unordered_map.hpp
/usr/include/msgpack/adaptor/cpp11/unordered_set.hpp
/usr/include/msgpack/adaptor/cpp17/byte.hpp
/usr/include/msgpack/adaptor/cpp17/carray_byte.hpp
/usr/include/msgpack/adaptor/cpp17/optional.hpp
/usr/include/msgpack/adaptor/cpp17/string_view.hpp
/usr/include/msgpack/adaptor/cpp17/vector_byte.hpp
/usr/include/msgpack/adaptor/define.hpp
/usr/include/msgpack/adaptor/define_decl.hpp
/usr/include/msgpack/adaptor/deque.hpp
/usr/include/msgpack/adaptor/ext.hpp
/usr/include/msgpack/adaptor/ext_decl.hpp
/usr/include/msgpack/adaptor/fixint.hpp
/usr/include/msgpack/adaptor/fixint_decl.hpp
/usr/include/msgpack/adaptor/float.hpp
/usr/include/msgpack/adaptor/int.hpp
/usr/include/msgpack/adaptor/int_decl.hpp
/usr/include/msgpack/adaptor/list.hpp
/usr/include/msgpack/adaptor/map.hpp
/usr/include/msgpack/adaptor/map_decl.hpp
/usr/include/msgpack/adaptor/msgpack_tuple.hpp
/usr/include/msgpack/adaptor/msgpack_tuple_decl.hpp
/usr/include/msgpack/adaptor/nil.hpp
/usr/include/msgpack/adaptor/nil_decl.hpp
/usr/include/msgpack/adaptor/pair.hpp
/usr/include/msgpack/adaptor/raw.hpp
/usr/include/msgpack/adaptor/raw_decl.hpp
/usr/include/msgpack/adaptor/set.hpp
/usr/include/msgpack/adaptor/size_equal_only.hpp
/usr/include/msgpack/adaptor/size_equal_only_decl.hpp
/usr/include/msgpack/adaptor/string.hpp
/usr/include/msgpack/adaptor/tr1/unordered_map.hpp
/usr/include/msgpack/adaptor/tr1/unordered_set.hpp
/usr/include/msgpack/adaptor/v4raw.hpp
/usr/include/msgpack/adaptor/v4raw_decl.hpp
/usr/include/msgpack/adaptor/vector.hpp
/usr/include/msgpack/adaptor/vector_bool.hpp
/usr/include/msgpack/adaptor/vector_char.hpp
/usr/include/msgpack/adaptor/vector_unsigned_char.hpp
/usr/include/msgpack/adaptor/wstring.hpp
/usr/include/msgpack/cpp_config.hpp
/usr/include/msgpack/cpp_config_decl.hpp
/usr/include/msgpack/create_object_visitor.hpp
/usr/include/msgpack/create_object_visitor_decl.hpp
/usr/include/msgpack/fbuffer.h
/usr/include/msgpack/fbuffer.hpp
/usr/include/msgpack/fbuffer_decl.hpp
/usr/include/msgpack/gcc_atomic.h
/usr/include/msgpack/gcc_atomic.hpp
/usr/include/msgpack/iterator.hpp
/usr/include/msgpack/iterator_decl.hpp
/usr/include/msgpack/meta.hpp
/usr/include/msgpack/meta_decl.hpp
/usr/include/msgpack/null_visitor.hpp
/usr/include/msgpack/null_visitor_decl.hpp
/usr/include/msgpack/object.h
/usr/include/msgpack/object.hpp
/usr/include/msgpack/object_decl.hpp
/usr/include/msgpack/object_fwd.hpp
/usr/include/msgpack/object_fwd_decl.hpp
/usr/include/msgpack/pack.h
/usr/include/msgpack/pack.hpp
/usr/include/msgpack/pack_decl.hpp
/usr/include/msgpack/pack_define.h
/usr/include/msgpack/pack_template.h
/usr/include/msgpack/parse.hpp
/usr/include/msgpack/parse_decl.hpp
/usr/include/msgpack/parse_return.hpp
/usr/include/msgpack/predef.h
/usr/include/msgpack/predef/architecture.h
/usr/include/msgpack/predef/architecture/alpha.h
/usr/include/msgpack/predef/architecture/arm.h
/usr/include/msgpack/predef/architecture/blackfin.h
/usr/include/msgpack/predef/architecture/convex.h
/usr/include/msgpack/predef/architecture/ia64.h
/usr/include/msgpack/predef/architecture/m68k.h
/usr/include/msgpack/predef/architecture/mips.h
/usr/include/msgpack/predef/architecture/parisc.h
/usr/include/msgpack/predef/architecture/ppc.h
/usr/include/msgpack/predef/architecture/ptx.h
/usr/include/msgpack/predef/architecture/pyramid.h
/usr/include/msgpack/predef/architecture/rs6k.h
/usr/include/msgpack/predef/architecture/sparc.h
/usr/include/msgpack/predef/architecture/superh.h
/usr/include/msgpack/predef/architecture/sys370.h
/usr/include/msgpack/predef/architecture/sys390.h
/usr/include/msgpack/predef/architecture/x86.h
/usr/include/msgpack/predef/architecture/x86/32.h
/usr/include/msgpack/predef/architecture/x86/64.h
/usr/include/msgpack/predef/architecture/z.h
/usr/include/msgpack/predef/compiler.h
/usr/include/msgpack/predef/compiler/borland.h
/usr/include/msgpack/predef/compiler/clang.h
/usr/include/msgpack/predef/compiler/comeau.h
/usr/include/msgpack/predef/compiler/compaq.h
/usr/include/msgpack/predef/compiler/diab.h
/usr/include/msgpack/predef/compiler/digitalmars.h
/usr/include/msgpack/predef/compiler/dignus.h
/usr/include/msgpack/predef/compiler/edg.h
/usr/include/msgpack/predef/compiler/ekopath.h
/usr/include/msgpack/predef/compiler/gcc.h
/usr/include/msgpack/predef/compiler/gcc_xml.h
/usr/include/msgpack/predef/compiler/greenhills.h
/usr/include/msgpack/predef/compiler/hp_acc.h
/usr/include/msgpack/predef/compiler/iar.h
/usr/include/msgpack/predef/compiler/ibm.h
/usr/include/msgpack/predef/compiler/intel.h
/usr/include/msgpack/predef/compiler/kai.h
/usr/include/msgpack/predef/compiler/llvm.h
/usr/include/msgpack/predef/compiler/metaware.h
/usr/include/msgpack/predef/compiler/metrowerks.h
/usr/include/msgpack/predef/compiler/microtec.h
/usr/include/msgpack/predef/compiler/mpw.h
/usr/include/msgpack/predef/compiler/nvcc.h
/usr/include/msgpack/predef/compiler/palm.h
/usr/include/msgpack/predef/compiler/pgi.h
/usr/include/msgpack/predef/compiler/sgi_mipspro.h
/usr/include/msgpack/predef/compiler/sunpro.h
/usr/include/msgpack/predef/compiler/tendra.h
/usr/include/msgpack/predef/compiler/visualc.h
/usr/include/msgpack/predef/compiler/watcom.h
/usr/include/msgpack/predef/detail/_cassert.h
/usr/include/msgpack/predef/detail/_exception.h
/usr/include/msgpack/predef/detail/comp_detected.h
/usr/include/msgpack/predef/detail/endian_compat.h
/usr/include/msgpack/predef/detail/os_detected.h
/usr/include/msgpack/predef/detail/platform_detected.h
/usr/include/msgpack/predef/detail/test.h
/usr/include/msgpack/predef/detail/test_def.h
/usr/include/msgpack/predef/hardware.h
/usr/include/msgpack/predef/hardware/simd.h
/usr/include/msgpack/predef/hardware/simd/arm.h
/usr/include/msgpack/predef/hardware/simd/arm/versions.h
/usr/include/msgpack/predef/hardware/simd/ppc.h
/usr/include/msgpack/predef/hardware/simd/ppc/versions.h
/usr/include/msgpack/predef/hardware/simd/x86.h
/usr/include/msgpack/predef/hardware/simd/x86/versions.h
/usr/include/msgpack/predef/hardware/simd/x86_amd.h
/usr/include/msgpack/predef/hardware/simd/x86_amd/versions.h
/usr/include/msgpack/predef/language.h
/usr/include/msgpack/predef/language/cuda.h
/usr/include/msgpack/predef/language/objc.h
/usr/include/msgpack/predef/language/stdc.h
/usr/include/msgpack/predef/language/stdcpp.h
/usr/include/msgpack/predef/library.h
/usr/include/msgpack/predef/library/c.h
/usr/include/msgpack/predef/library/c/_prefix.h
/usr/include/msgpack/predef/library/c/cloudabi.h
/usr/include/msgpack/predef/library/c/gnu.h
/usr/include/msgpack/predef/library/c/uc.h
/usr/include/msgpack/predef/library/c/vms.h
/usr/include/msgpack/predef/library/c/zos.h
/usr/include/msgpack/predef/library/std.h
/usr/include/msgpack/predef/library/std/_prefix.h
/usr/include/msgpack/predef/library/std/cxx.h
/usr/include/msgpack/predef/library/std/dinkumware.h
/usr/include/msgpack/predef/library/std/libcomo.h
/usr/include/msgpack/predef/library/std/modena.h
/usr/include/msgpack/predef/library/std/msl.h
/usr/include/msgpack/predef/library/std/roguewave.h
/usr/include/msgpack/predef/library/std/sgi.h
/usr/include/msgpack/predef/library/std/stdcpp3.h
/usr/include/msgpack/predef/library/std/stlport.h
/usr/include/msgpack/predef/library/std/vacpp.h
/usr/include/msgpack/predef/make.h
/usr/include/msgpack/predef/os.h
/usr/include/msgpack/predef/os/aix.h
/usr/include/msgpack/predef/os/amigaos.h
/usr/include/msgpack/predef/os/android.h
/usr/include/msgpack/predef/os/beos.h
/usr/include/msgpack/predef/os/bsd.h
/usr/include/msgpack/predef/os/bsd/bsdi.h
/usr/include/msgpack/predef/os/bsd/dragonfly.h
/usr/include/msgpack/predef/os/bsd/free.h
/usr/include/msgpack/predef/os/bsd/net.h
/usr/include/msgpack/predef/os/bsd/open.h
/usr/include/msgpack/predef/os/cygwin.h
/usr/include/msgpack/predef/os/haiku.h
/usr/include/msgpack/predef/os/hpux.h
/usr/include/msgpack/predef/os/ios.h
/usr/include/msgpack/predef/os/irix.h
/usr/include/msgpack/predef/os/linux.h
/usr/include/msgpack/predef/os/macos.h
/usr/include/msgpack/predef/os/os400.h
/usr/include/msgpack/predef/os/qnxnto.h
/usr/include/msgpack/predef/os/solaris.h
/usr/include/msgpack/predef/os/unix.h
/usr/include/msgpack/predef/os/vms.h
/usr/include/msgpack/predef/os/windows.h
/usr/include/msgpack/predef/other.h
/usr/include/msgpack/predef/other/endian.h
/usr/include/msgpack/predef/other/workaround.h
/usr/include/msgpack/predef/platform.h
/usr/include/msgpack/predef/platform/cloudabi.h
/usr/include/msgpack/predef/platform/ios.h
/usr/include/msgpack/predef/platform/mingw.h
/usr/include/msgpack/predef/platform/mingw32.h
/usr/include/msgpack/predef/platform/mingw64.h
/usr/include/msgpack/predef/platform/windows_desktop.h
/usr/include/msgpack/predef/platform/windows_phone.h
/usr/include/msgpack/predef/platform/windows_runtime.h
/usr/include/msgpack/predef/platform/windows_server.h
/usr/include/msgpack/predef/platform/windows_store.h
/usr/include/msgpack/predef/platform/windows_system.h
/usr/include/msgpack/predef/platform/windows_uwp.h
/usr/include/msgpack/predef/version.h
/usr/include/msgpack/predef/version_number.h
/usr/include/msgpack/preprocessor.hpp
/usr/include/msgpack/preprocessor/arithmetic.hpp
/usr/include/msgpack/preprocessor/arithmetic/add.hpp
/usr/include/msgpack/preprocessor/arithmetic/dec.hpp
/usr/include/msgpack/preprocessor/arithmetic/detail/div_base.hpp
/usr/include/msgpack/preprocessor/arithmetic/div.hpp
/usr/include/msgpack/preprocessor/arithmetic/inc.hpp
/usr/include/msgpack/preprocessor/arithmetic/mod.hpp
/usr/include/msgpack/preprocessor/arithmetic/mul.hpp
/usr/include/msgpack/preprocessor/arithmetic/sub.hpp
/usr/include/msgpack/preprocessor/array.hpp
/usr/include/msgpack/preprocessor/array/data.hpp
/usr/include/msgpack/preprocessor/array/detail/get_data.hpp
/usr/include/msgpack/preprocessor/array/elem.hpp
/usr/include/msgpack/preprocessor/array/enum.hpp
/usr/include/msgpack/preprocessor/array/insert.hpp
/usr/include/msgpack/preprocessor/array/pop_back.hpp
/usr/include/msgpack/preprocessor/array/pop_front.hpp
/usr/include/msgpack/preprocessor/array/push_back.hpp
/usr/include/msgpack/preprocessor/array/push_front.hpp
/usr/include/msgpack/preprocessor/array/remove.hpp
/usr/include/msgpack/preprocessor/array/replace.hpp
/usr/include/msgpack/preprocessor/array/reverse.hpp
/usr/include/msgpack/preprocessor/array/size.hpp
/usr/include/msgpack/preprocessor/array/to_list.hpp
/usr/include/msgpack/preprocessor/array/to_seq.hpp
/usr/include/msgpack/preprocessor/array/to_tuple.hpp
/usr/include/msgpack/preprocessor/assert_msg.hpp
/usr/include/msgpack/preprocessor/cat.hpp
/usr/include/msgpack/preprocessor/comma.hpp
/usr/include/msgpack/preprocessor/comma_if.hpp
/usr/include/msgpack/preprocessor/comparison.hpp
/usr/include/msgpack/preprocessor/comparison/equal.hpp
/usr/include/msgpack/preprocessor/comparison/greater.hpp
/usr/include/msgpack/preprocessor/comparison/greater_equal.hpp
/usr/include/msgpack/preprocessor/comparison/less.hpp
/usr/include/msgpack/preprocessor/comparison/less_equal.hpp
/usr/include/msgpack/preprocessor/comparison/not_equal.hpp
/usr/include/msgpack/preprocessor/config/config.hpp
/usr/include/msgpack/preprocessor/config/limits.hpp
/usr/include/msgpack/preprocessor/control.hpp
/usr/include/msgpack/preprocessor/control/deduce_d.hpp
/usr/include/msgpack/preprocessor/control/detail/dmc/while.hpp
/usr/include/msgpack/preprocessor/control/detail/edg/while.hpp
/usr/include/msgpack/preprocessor/control/detail/msvc/while.hpp
/usr/include/msgpack/preprocessor/control/detail/while.hpp
/usr/include/msgpack/preprocessor/control/expr_if.hpp
/usr/include/msgpack/preprocessor/control/expr_iif.hpp
/usr/include/msgpack/preprocessor/control/if.hpp
/usr/include/msgpack/preprocessor/control/iif.hpp
/usr/include/msgpack/preprocessor/control/while.hpp
/usr/include/msgpack/preprocessor/debug.hpp
/usr/include/msgpack/preprocessor/debug/assert.hpp
/usr/include/msgpack/preprocessor/debug/error.hpp
/usr/include/msgpack/preprocessor/debug/line.hpp
/usr/include/msgpack/preprocessor/dec.hpp
/usr/include/msgpack/preprocessor/detail/auto_rec.hpp
/usr/include/msgpack/preprocessor/detail/check.hpp
/usr/include/msgpack/preprocessor/detail/dmc/auto_rec.hpp
/usr/include/msgpack/preprocessor/detail/is_binary.hpp
/usr/include/msgpack/preprocessor/detail/is_nullary.hpp
/usr/include/msgpack/preprocessor/detail/is_unary.hpp
/usr/include/msgpack/preprocessor/detail/null.hpp
/usr/include/msgpack/preprocessor/detail/split.hpp
/usr/include/msgpack/preprocessor/empty.hpp
/usr/include/msgpack/preprocessor/enum.hpp
/usr/include/msgpack/preprocessor/enum_params.hpp
/usr/include/msgpack/preprocessor/enum_params_with_a_default.hpp
/usr/include/msgpack/preprocessor/enum_params_with_defaults.hpp
/usr/include/msgpack/preprocessor/enum_shifted.hpp
/usr/include/msgpack/preprocessor/enum_shifted_params.hpp
/usr/include/msgpack/preprocessor/expand.hpp
/usr/include/msgpack/preprocessor/expr_if.hpp
/usr/include/msgpack/preprocessor/facilities.hpp
/usr/include/msgpack/preprocessor/facilities/apply.hpp
/usr/include/msgpack/preprocessor/facilities/detail/is_empty.hpp
/usr/include/msgpack/preprocessor/facilities/empty.hpp
/usr/include/msgpack/preprocessor/facilities/expand.hpp
/usr/include/msgpack/preprocessor/facilities/identity.hpp
/usr/include/msgpack/preprocessor/facilities/intercept.hpp
/usr/include/msgpack/preprocessor/facilities/is_1.hpp
/usr/include/msgpack/preprocessor/facilities/is_empty.hpp
/usr/include/msgpack/preprocessor/facilities/is_empty_or_1.hpp
/usr/include/msgpack/preprocessor/facilities/is_empty_variadic.hpp
/usr/include/msgpack/preprocessor/facilities/overload.hpp
/usr/include/msgpack/preprocessor/for.hpp
/usr/include/msgpack/preprocessor/identity.hpp
/usr/include/msgpack/preprocessor/if.hpp
/usr/include/msgpack/preprocessor/inc.hpp
/usr/include/msgpack/preprocessor/iterate.hpp
/usr/include/msgpack/preprocessor/iteration.hpp
/usr/include/msgpack/preprocessor/iteration/detail/bounds/lower1.hpp
/usr/include/msgpack/preprocessor/iteration/detail/bounds/lower2.hpp
/usr/include/msgpack/preprocessor/iteration/detail/bounds/lower3.hpp
/usr/include/msgpack/preprocessor/iteration/detail/bounds/lower4.hpp
/usr/include/msgpack/preprocessor/iteration/detail/bounds/lower5.hpp
/usr/include/msgpack/preprocessor/iteration/detail/bounds/upper1.hpp
/usr/include/msgpack/preprocessor/iteration/detail/bounds/upper2.hpp
/usr/include/msgpack/preprocessor/iteration/detail/bounds/upper3.hpp
/usr/include/msgpack/preprocessor/iteration/detail/bounds/upper4.hpp
/usr/include/msgpack/preprocessor/iteration/detail/bounds/upper5.hpp
/usr/include/msgpack/preprocessor/iteration/detail/finish.hpp
/usr/include/msgpack/preprocessor/iteration/detail/iter/forward1.hpp
/usr/include/msgpack/preprocessor/iteration/detail/iter/forward2.hpp
/usr/include/msgpack/preprocessor/iteration/detail/iter/forward3.hpp
/usr/include/msgpack/preprocessor/iteration/detail/iter/forward4.hpp
/usr/include/msgpack/preprocessor/iteration/detail/iter/forward5.hpp
/usr/include/msgpack/preprocessor/iteration/detail/iter/reverse1.hpp
/usr/include/msgpack/preprocessor/iteration/detail/iter/reverse2.hpp
/usr/include/msgpack/preprocessor/iteration/detail/iter/reverse3.hpp
/usr/include/msgpack/preprocessor/iteration/detail/iter/reverse4.hpp
/usr/include/msgpack/preprocessor/iteration/detail/iter/reverse5.hpp
/usr/include/msgpack/preprocessor/iteration/detail/local.hpp
/usr/include/msgpack/preprocessor/iteration/detail/rlocal.hpp
/usr/include/msgpack/preprocessor/iteration/detail/self.hpp
/usr/include/msgpack/preprocessor/iteration/detail/start.hpp
/usr/include/msgpack/preprocessor/iteration/iterate.hpp
/usr/include/msgpack/preprocessor/iteration/local.hpp
/usr/include/msgpack/preprocessor/iteration/self.hpp
/usr/include/msgpack/preprocessor/library.hpp
/usr/include/msgpack/preprocessor/limits.hpp
/usr/include/msgpack/preprocessor/list.hpp
/usr/include/msgpack/preprocessor/list/adt.hpp
/usr/include/msgpack/preprocessor/list/append.hpp
/usr/include/msgpack/preprocessor/list/at.hpp
/usr/include/msgpack/preprocessor/list/cat.hpp
/usr/include/msgpack/preprocessor/list/detail/dmc/fold_left.hpp
/usr/include/msgpack/preprocessor/list/detail/edg/fold_left.hpp
/usr/include/msgpack/preprocessor/list/detail/edg/fold_right.hpp
/usr/include/msgpack/preprocessor/list/detail/fold_left.hpp
/usr/include/msgpack/preprocessor/list/detail/fold_right.hpp
/usr/include/msgpack/preprocessor/list/enum.hpp
/usr/include/msgpack/preprocessor/list/filter.hpp
/usr/include/msgpack/preprocessor/list/first_n.hpp
/usr/include/msgpack/preprocessor/list/fold_left.hpp
/usr/include/msgpack/preprocessor/list/fold_right.hpp
/usr/include/msgpack/preprocessor/list/for_each.hpp
/usr/include/msgpack/preprocessor/list/for_each_i.hpp
/usr/include/msgpack/preprocessor/list/for_each_product.hpp
/usr/include/msgpack/preprocessor/list/rest_n.hpp
/usr/include/msgpack/preprocessor/list/reverse.hpp
/usr/include/msgpack/preprocessor/list/size.hpp
/usr/include/msgpack/preprocessor/list/to_array.hpp
/usr/include/msgpack/preprocessor/list/to_seq.hpp
/usr/include/msgpack/preprocessor/list/to_tuple.hpp
/usr/include/msgpack/preprocessor/list/transform.hpp
/usr/include/msgpack/preprocessor/logical.hpp
/usr/include/msgpack/preprocessor/logical/and.hpp
/usr/include/msgpack/preprocessor/logical/bitand.hpp
/usr/include/msgpack/preprocessor/logical/bitnor.hpp
/usr/include/msgpack/preprocessor/logical/bitor.hpp
/usr/include/msgpack/preprocessor/logical/bitxor.hpp
/usr/include/msgpack/preprocessor/logical/bool.hpp
/usr/include/msgpack/preprocessor/logical/compl.hpp
/usr/include/msgpack/preprocessor/logical/nor.hpp
/usr/include/msgpack/preprocessor/logical/not.hpp
/usr/include/msgpack/preprocessor/logical/or.hpp
/usr/include/msgpack/preprocessor/logical/xor.hpp
/usr/include/msgpack/preprocessor/max.hpp
/usr/include/msgpack/preprocessor/min.hpp
/usr/include/msgpack/preprocessor/punctuation.hpp
/usr/include/msgpack/preprocessor/punctuation/comma.hpp
/usr/include/msgpack/preprocessor/punctuation/comma_if.hpp
/usr/include/msgpack/preprocessor/punctuation/detail/is_begin_parens.hpp
/usr/include/msgpack/preprocessor/punctuation/is_begin_parens.hpp
/usr/include/msgpack/preprocessor/punctuation/paren.hpp
/usr/include/msgpack/preprocessor/punctuation/paren_if.hpp
/usr/include/msgpack/preprocessor/punctuation/remove_parens.hpp
/usr/include/msgpack/preprocessor/repeat.hpp
/usr/include/msgpack/preprocessor/repeat_2nd.hpp
/usr/include/msgpack/preprocessor/repeat_3rd.hpp
/usr/include/msgpack/preprocessor/repeat_from_to.hpp
/usr/include/msgpack/preprocessor/repeat_from_to_2nd.hpp
/usr/include/msgpack/preprocessor/repeat_from_to_3rd.hpp
/usr/include/msgpack/preprocessor/repetition.hpp
/usr/include/msgpack/preprocessor/repetition/deduce_r.hpp
/usr/include/msgpack/preprocessor/repetition/deduce_z.hpp
/usr/include/msgpack/preprocessor/repetition/detail/dmc/for.hpp
/usr/include/msgpack/preprocessor/repetition/detail/edg/for.hpp
/usr/include/msgpack/preprocessor/repetition/detail/for.hpp
/usr/include/msgpack/preprocessor/repetition/detail/msvc/for.hpp
/usr/include/msgpack/preprocessor/repetition/enum.hpp
/usr/include/msgpack/preprocessor/repetition/enum_binary_params.hpp
/usr/include/msgpack/preprocessor/repetition/enum_params.hpp
/usr/include/msgpack/preprocessor/repetition/enum_params_with_a_default.hpp
/usr/include/msgpack/preprocessor/repetition/enum_params_with_defaults.hpp
/usr/include/msgpack/preprocessor/repetition/enum_shifted.hpp
/usr/include/msgpack/preprocessor/repetition/enum_shifted_binary_params.hpp
/usr/include/msgpack/preprocessor/repetition/enum_shifted_params.hpp
/usr/include/msgpack/preprocessor/repetition/enum_trailing.hpp
/usr/include/msgpack/preprocessor/repetition/enum_trailing_binary_params.hpp
/usr/include/msgpack/preprocessor/repetition/enum_trailing_params.hpp
/usr/include/msgpack/preprocessor/repetition/for.hpp
/usr/include/msgpack/preprocessor/repetition/repeat.hpp
/usr/include/msgpack/preprocessor/repetition/repeat_from_to.hpp
/usr/include/msgpack/preprocessor/selection.hpp
/usr/include/msgpack/preprocessor/selection/max.hpp
/usr/include/msgpack/preprocessor/selection/min.hpp
/usr/include/msgpack/preprocessor/seq.hpp
/usr/include/msgpack/preprocessor/seq/cat.hpp
/usr/include/msgpack/preprocessor/seq/detail/binary_transform.hpp
/usr/include/msgpack/preprocessor/seq/detail/is_empty.hpp
/usr/include/msgpack/preprocessor/seq/detail/split.hpp
/usr/include/msgpack/preprocessor/seq/detail/to_list_msvc.hpp
/usr/include/msgpack/preprocessor/seq/elem.hpp
/usr/include/msgpack/preprocessor/seq/enum.hpp
/usr/include/msgpack/preprocessor/seq/filter.hpp
/usr/include/msgpack/preprocessor/seq/first_n.hpp
/usr/include/msgpack/preprocessor/seq/fold_left.hpp
/usr/include/msgpack/preprocessor/seq/fold_right.hpp
/usr/include/msgpack/preprocessor/seq/for_each.hpp
/usr/include/msgpack/preprocessor/seq/for_each_i.hpp
/usr/include/msgpack/preprocessor/seq/for_each_product.hpp
/usr/include/msgpack/preprocessor/seq/insert.hpp
/usr/include/msgpack/preprocessor/seq/pop_back.hpp
/usr/include/msgpack/preprocessor/seq/pop_front.hpp
/usr/include/msgpack/preprocessor/seq/push_back.hpp
/usr/include/msgpack/preprocessor/seq/push_front.hpp
/usr/include/msgpack/preprocessor/seq/remove.hpp
/usr/include/msgpack/preprocessor/seq/replace.hpp
/usr/include/msgpack/preprocessor/seq/rest_n.hpp
/usr/include/msgpack/preprocessor/seq/reverse.hpp
/usr/include/msgpack/preprocessor/seq/seq.hpp
/usr/include/msgpack/preprocessor/seq/size.hpp
/usr/include/msgpack/preprocessor/seq/subseq.hpp
/usr/include/msgpack/preprocessor/seq/to_array.hpp
/usr/include/msgpack/preprocessor/seq/to_list.hpp
/usr/include/msgpack/preprocessor/seq/to_tuple.hpp
/usr/include/msgpack/preprocessor/seq/transform.hpp
/usr/include/msgpack/preprocessor/seq/variadic_seq_to_seq.hpp
/usr/include/msgpack/preprocessor/slot.hpp
/usr/include/msgpack/preprocessor/slot/counter.hpp
/usr/include/msgpack/preprocessor/slot/detail/counter.hpp
/usr/include/msgpack/preprocessor/slot/detail/def.hpp
/usr/include/msgpack/preprocessor/slot/detail/shared.hpp
/usr/include/msgpack/preprocessor/slot/detail/slot1.hpp
/usr/include/msgpack/preprocessor/slot/detail/slot2.hpp
/usr/include/msgpack/preprocessor/slot/detail/slot3.hpp
/usr/include/msgpack/preprocessor/slot/detail/slot4.hpp
/usr/include/msgpack/preprocessor/slot/detail/slot5.hpp
/usr/include/msgpack/preprocessor/slot/slot.hpp
/usr/include/msgpack/preprocessor/stringize.hpp
/usr/include/msgpack/preprocessor/tuple.hpp
/usr/include/msgpack/preprocessor/tuple/detail/is_single_return.hpp
/usr/include/msgpack/preprocessor/tuple/eat.hpp
/usr/include/msgpack/preprocessor/tuple/elem.hpp
/usr/include/msgpack/preprocessor/tuple/enum.hpp
/usr/include/msgpack/preprocessor/tuple/insert.hpp
/usr/include/msgpack/preprocessor/tuple/pop_back.hpp
/usr/include/msgpack/preprocessor/tuple/pop_front.hpp
/usr/include/msgpack/preprocessor/tuple/push_back.hpp
/usr/include/msgpack/preprocessor/tuple/push_front.hpp
/usr/include/msgpack/preprocessor/tuple/rem.hpp
/usr/include/msgpack/preprocessor/tuple/remove.hpp
/usr/include/msgpack/preprocessor/tuple/replace.hpp
/usr/include/msgpack/preprocessor/tuple/reverse.hpp
/usr/include/msgpack/preprocessor/tuple/size.hpp
/usr/include/msgpack/preprocessor/tuple/to_array.hpp
/usr/include/msgpack/preprocessor/tuple/to_list.hpp
/usr/include/msgpack/preprocessor/tuple/to_seq.hpp
/usr/include/msgpack/preprocessor/variadic.hpp
/usr/include/msgpack/preprocessor/variadic/detail/is_single_return.hpp
/usr/include/msgpack/preprocessor/variadic/elem.hpp
/usr/include/msgpack/preprocessor/variadic/size.hpp
/usr/include/msgpack/preprocessor/variadic/to_array.hpp
/usr/include/msgpack/preprocessor/variadic/to_list.hpp
/usr/include/msgpack/preprocessor/variadic/to_seq.hpp
/usr/include/msgpack/preprocessor/variadic/to_tuple.hpp
/usr/include/msgpack/preprocessor/while.hpp
/usr/include/msgpack/preprocessor/wstringize.hpp
/usr/include/msgpack/sbuffer.h
/usr/include/msgpack/sbuffer.hpp
/usr/include/msgpack/sbuffer_decl.hpp
/usr/include/msgpack/sysdep.h
/usr/include/msgpack/timestamp.h
/usr/include/msgpack/type.hpp
/usr/include/msgpack/unpack.h
/usr/include/msgpack/unpack.hpp
/usr/include/msgpack/unpack_decl.hpp
/usr/include/msgpack/unpack_define.h
/usr/include/msgpack/unpack_exception.hpp
/usr/include/msgpack/unpack_template.h
/usr/include/msgpack/util.h
/usr/include/msgpack/v1/adaptor/adaptor_base.hpp
/usr/include/msgpack/v1/adaptor/adaptor_base_decl.hpp
/usr/include/msgpack/v1/adaptor/array_ref.hpp
/usr/include/msgpack/v1/adaptor/array_ref_decl.hpp
/usr/include/msgpack/v1/adaptor/bool.hpp
/usr/include/msgpack/v1/adaptor/boost/fusion.hpp
/usr/include/msgpack/v1/adaptor/boost/msgpack_variant.hpp
/usr/include/msgpack/v1/adaptor/boost/msgpack_variant_decl.hpp
/usr/include/msgpack/v1/adaptor/boost/optional.hpp
/usr/include/msgpack/v1/adaptor/boost/string_ref.hpp
/usr/include/msgpack/v1/adaptor/boost/string_view.hpp
/usr/include/msgpack/v1/adaptor/carray.hpp
/usr/include/msgpack/v1/adaptor/char_ptr.hpp
/usr/include/msgpack/v1/adaptor/check_container_size.hpp
/usr/include/msgpack/v1/adaptor/check_container_size_decl.hpp
/usr/include/msgpack/v1/adaptor/cpp11/array.hpp
/usr/include/msgpack/v1/adaptor/cpp11/array_char.hpp
/usr/include/msgpack/v1/adaptor/cpp11/array_unsigned_char.hpp
/usr/include/msgpack/v1/adaptor/cpp11/chrono.hpp
/usr/include/msgpack/v1/adaptor/cpp11/forward_list.hpp
/usr/include/msgpack/v1/adaptor/cpp11/reference_wrapper.hpp
/usr/include/msgpack/v1/adaptor/cpp11/shared_ptr.hpp
/usr/include/msgpack/v1/adaptor/cpp11/timespec.hpp
/usr/include/msgpack/v1/adaptor/cpp11/tuple.hpp
/usr/include/msgpack/v1/adaptor/cpp11/unique_ptr.hpp
/usr/include/msgpack/v1/adaptor/cpp11/unordered_map.hpp
/usr/include/msgpack/v1/adaptor/cpp11/unordered_set.hpp
/usr/include/msgpack/v1/adaptor/cpp17/byte.hpp
/usr/include/msgpack/v1/adaptor/cpp17/carray_byte.hpp
/usr/include/msgpack/v1/adaptor/cpp17/optional.hpp
/usr/include/msgpack/v1/adaptor/cpp17/string_view.hpp
/usr/include/msgpack/v1/adaptor/cpp17/vector_byte.hpp
/usr/include/msgpack/v1/adaptor/define.hpp
/usr/include/msgpack/v1/adaptor/define_decl.hpp
/usr/include/msgpack/v1/adaptor/deque.hpp
/usr/include/msgpack/v1/adaptor/detail/cpp03_define_array.hpp
/usr/include/msgpack/v1/adaptor/detail/cpp03_define_array_decl.hpp
/usr/include/msgpack/v1/adaptor/detail/cpp03_define_map.hpp
/usr/include/msgpack/v1/adaptor/detail/cpp03_define_map_decl.hpp
/usr/include/msgpack/v1/adaptor/detail/cpp03_msgpack_tuple.hpp
/usr/include/msgpack/v1/adaptor/detail/cpp03_msgpack_tuple_decl.hpp
/usr/include/msgpack/v1/adaptor/detail/cpp11_convert_helper.hpp
/usr/include/msgpack/v1/adaptor/detail/cpp11_define_array.hpp
/usr/include/msgpack/v1/adaptor/detail/cpp11_define_array_decl.hpp
/usr/include/msgpack/v1/adaptor/detail/cpp11_define_map.hpp
/usr/include/msgpack/v1/adaptor/detail/cpp11_define_map_decl.hpp
/usr/include/msgpack/v1/adaptor/detail/cpp11_msgpack_tuple.hpp
/usr/include/msgpack/v1/adaptor/detail/cpp11_msgpack_tuple_decl.hpp
/usr/include/msgpack/v1/adaptor/ext.hpp
/usr/include/msgpack/v1/adaptor/ext_decl.hpp
/usr/include/msgpack/v1/adaptor/fixint.hpp
/usr/include/msgpack/v1/adaptor/fixint_decl.hpp
/usr/include/msgpack/v1/adaptor/float.hpp
/usr/include/msgpack/v1/adaptor/int.hpp
/usr/include/msgpack/v1/adaptor/int_decl.hpp
/usr/include/msgpack/v1/adaptor/list.hpp
/usr/include/msgpack/v1/adaptor/map.hpp
/usr/include/msgpack/v1/adaptor/map_decl.hpp
/usr/include/msgpack/v1/adaptor/msgpack_tuple.hpp
/usr/include/msgpack/v1/adaptor/msgpack_tuple_decl.hpp
/usr/include/msgpack/v1/adaptor/nil.hpp
/usr/include/msgpack/v1/adaptor/nil_decl.hpp
/usr/include/msgpack/v1/adaptor/pair.hpp
/usr/include/msgpack/v1/adaptor/raw.hpp
/usr/include/msgpack/v1/adaptor/raw_decl.hpp
/usr/include/msgpack/v1/adaptor/set.hpp
/usr/include/msgpack/v1/adaptor/size_equal_only.hpp
/usr/include/msgpack/v1/adaptor/size_equal_only_decl.hpp
/usr/include/msgpack/v1/adaptor/string.hpp
/usr/include/msgpack/v1/adaptor/tr1/unordered_map.hpp
/usr/include/msgpack/v1/adaptor/tr1/unordered_set.hpp
/usr/include/msgpack/v1/adaptor/v4raw.hpp
/usr/include/msgpack/v1/adaptor/v4raw_decl.hpp
/usr/include/msgpack/v1/adaptor/vector.hpp
/usr/include/msgpack/v1/adaptor/vector_bool.hpp
/usr/include/msgpack/v1/adaptor/vector_char.hpp
/usr/include/msgpack/v1/adaptor/vector_unsigned_char.hpp
/usr/include/msgpack/v1/adaptor/wstring.hpp
/usr/include/msgpack/v1/cpp_config.hpp
/usr/include/msgpack/v1/cpp_config_decl.hpp
/usr/include/msgpack/v1/detail/cpp03_zone.hpp
/usr/include/msgpack/v1/detail/cpp03_zone_decl.hpp
/usr/include/msgpack/v1/detail/cpp11_zone.hpp
/usr/include/msgpack/v1/detail/cpp11_zone_decl.hpp
/usr/include/msgpack/v1/fbuffer.hpp
/usr/include/msgpack/v1/fbuffer_decl.hpp
/usr/include/msgpack/v1/iterator.hpp
/usr/include/msgpack/v1/iterator_decl.hpp
/usr/include/msgpack/v1/meta.hpp
/usr/include/msgpack/v1/meta_decl.hpp
/usr/include/msgpack/v1/object.hpp
/usr/include/msgpack/v1/object_decl.hpp
/usr/include/msgpack/v1/object_fwd.hpp
/usr/include/msgpack/v1/object_fwd_decl.hpp
/usr/include/msgpack/v1/pack.hpp
/usr/include/msgpack/v1/pack_decl.hpp
/usr/include/msgpack/v1/parse_return.hpp
/usr/include/msgpack/v1/preprocessor.hpp
/usr/include/msgpack/v1/sbuffer.hpp
/usr/include/msgpack/v1/sbuffer_decl.hpp
/usr/include/msgpack/v1/unpack.hpp
/usr/include/msgpack/v1/unpack_decl.hpp
/usr/include/msgpack/v1/unpack_exception.hpp
/usr/include/msgpack/v1/version.hpp
/usr/include/msgpack/v1/versioning.hpp
/usr/include/msgpack/v1/vrefbuffer.hpp
/usr/include/msgpack/v1/vrefbuffer_decl.hpp
/usr/include/msgpack/v1/zbuffer.hpp
/usr/include/msgpack/v1/zbuffer_decl.hpp
/usr/include/msgpack/v1/zone.hpp
/usr/include/msgpack/v1/zone_decl.hpp
/usr/include/msgpack/v2/adaptor/adaptor_base.hpp
/usr/include/msgpack/v2/adaptor/adaptor_base_decl.hpp
/usr/include/msgpack/v2/adaptor/array_ref_decl.hpp
/usr/include/msgpack/v2/adaptor/boost/msgpack_variant_decl.hpp
/usr/include/msgpack/v2/adaptor/check_container_size_decl.hpp
/usr/include/msgpack/v2/adaptor/define_decl.hpp
/usr/include/msgpack/v2/adaptor/detail/cpp03_define_array_decl.hpp
/usr/include/msgpack/v2/adaptor/detail/cpp03_define_map_decl.hpp
/usr/include/msgpack/v2/adaptor/detail/cpp03_msgpack_tuple_decl.hpp
/usr/include/msgpack/v2/adaptor/detail/cpp11_define_array_decl.hpp
/usr/include/msgpack/v2/adaptor/detail/cpp11_define_map_decl.hpp
/usr/include/msgpack/v2/adaptor/detail/cpp11_msgpack_tuple_decl.hpp
/usr/include/msgpack/v2/adaptor/ext_decl.hpp
/usr/include/msgpack/v2/adaptor/fixint_decl.hpp
/usr/include/msgpack/v2/adaptor/int_decl.hpp
/usr/include/msgpack/v2/adaptor/map_decl.hpp
/usr/include/msgpack/v2/adaptor/msgpack_tuple_decl.hpp
/usr/include/msgpack/v2/adaptor/nil_decl.hpp
/usr/include/msgpack/v2/adaptor/raw_decl.hpp
/usr/include/msgpack/v2/adaptor/size_equal_only_decl.hpp
/usr/include/msgpack/v2/adaptor/v4raw_decl.hpp
/usr/include/msgpack/v2/cpp_config_decl.hpp
/usr/include/msgpack/v2/create_object_visitor.hpp
/usr/include/msgpack/v2/create_object_visitor_decl.hpp
/usr/include/msgpack/v2/detail/cpp03_zone_decl.hpp
/usr/include/msgpack/v2/detail/cpp11_zone_decl.hpp
/usr/include/msgpack/v2/fbuffer_decl.hpp
/usr/include/msgpack/v2/iterator_decl.hpp
/usr/include/msgpack/v2/meta_decl.hpp
/usr/include/msgpack/v2/null_visitor.hpp
/usr/include/msgpack/v2/null_visitor_decl.hpp
/usr/include/msgpack/v2/object.hpp
/usr/include/msgpack/v2/object_decl.hpp
/usr/include/msgpack/v2/object_fwd.hpp
/usr/include/msgpack/v2/object_fwd_decl.hpp
/usr/include/msgpack/v2/pack_decl.hpp
/usr/include/msgpack/v2/parse.hpp
/usr/include/msgpack/v2/parse_decl.hpp
/usr/include/msgpack/v2/parse_return.hpp
/usr/include/msgpack/v2/sbuffer_decl.hpp
/usr/include/msgpack/v2/unpack.hpp
/usr/include/msgpack/v2/unpack_decl.hpp
/usr/include/msgpack/v2/vrefbuffer_decl.hpp
/usr/include/msgpack/v2/x3_parse.hpp
/usr/include/msgpack/v2/x3_parse_decl.hpp
/usr/include/msgpack/v2/x3_unpack.hpp
/usr/include/msgpack/v2/x3_unpack_decl.hpp
/usr/include/msgpack/v2/zbuffer_decl.hpp
/usr/include/msgpack/v2/zone_decl.hpp
/usr/include/msgpack/v3/adaptor/adaptor_base.hpp
/usr/include/msgpack/v3/adaptor/adaptor_base_decl.hpp
/usr/include/msgpack/v3/adaptor/array_ref_decl.hpp
/usr/include/msgpack/v3/adaptor/boost/msgpack_variant_decl.hpp
/usr/include/msgpack/v3/adaptor/check_container_size_decl.hpp
/usr/include/msgpack/v3/adaptor/define_decl.hpp
/usr/include/msgpack/v3/adaptor/detail/cpp03_define_array_decl.hpp
/usr/include/msgpack/v3/adaptor/detail/cpp03_define_map_decl.hpp
/usr/include/msgpack/v3/adaptor/detail/cpp03_msgpack_tuple_decl.hpp
/usr/include/msgpack/v3/adaptor/detail/cpp11_define_array_decl.hpp
/usr/include/msgpack/v3/adaptor/detail/cpp11_define_map_decl.hpp
/usr/include/msgpack/v3/adaptor/detail/cpp11_msgpack_tuple_decl.hpp
/usr/include/msgpack/v3/adaptor/ext_decl.hpp
/usr/include/msgpack/v3/adaptor/fixint_decl.hpp
/usr/include/msgpack/v3/adaptor/int_decl.hpp
/usr/include/msgpack/v3/adaptor/map_decl.hpp
/usr/include/msgpack/v3/adaptor/msgpack_tuple_decl.hpp
/usr/include/msgpack/v3/adaptor/nil_decl.hpp
/usr/include/msgpack/v3/adaptor/raw_decl.hpp
/usr/include/msgpack/v3/adaptor/size_equal_only_decl.hpp
/usr/include/msgpack/v3/adaptor/v4raw_decl.hpp
/usr/include/msgpack/v3/cpp_config_decl.hpp
/usr/include/msgpack/v3/create_object_visitor_decl.hpp
/usr/include/msgpack/v3/detail/cpp03_zone_decl.hpp
/usr/include/msgpack/v3/detail/cpp11_zone_decl.hpp
/usr/include/msgpack/v3/fbuffer_decl.hpp
/usr/include/msgpack/v3/iterator_decl.hpp
/usr/include/msgpack/v3/meta_decl.hpp
/usr/include/msgpack/v3/null_visitor_decl.hpp
/usr/include/msgpack/v3/object_decl.hpp
/usr/include/msgpack/v3/object_fwd.hpp
/usr/include/msgpack/v3/object_fwd_decl.hpp
/usr/include/msgpack/v3/pack_decl.hpp
/usr/include/msgpack/v3/parse.hpp
/usr/include/msgpack/v3/parse_decl.hpp
/usr/include/msgpack/v3/parse_return.hpp
/usr/include/msgpack/v3/sbuffer_decl.hpp
/usr/include/msgpack/v3/unpack.hpp
/usr/include/msgpack/v3/unpack_decl.hpp
/usr/include/msgpack/v3/vrefbuffer_decl.hpp
/usr/include/msgpack/v3/x3_parse_decl.hpp
/usr/include/msgpack/v3/x3_unpack.hpp
/usr/include/msgpack/v3/x3_unpack_decl.hpp
/usr/include/msgpack/v3/zbuffer_decl.hpp
/usr/include/msgpack/v3/zone_decl.hpp
/usr/include/msgpack/version.h
/usr/include/msgpack/version.hpp
/usr/include/msgpack/version_master.h
/usr/include/msgpack/versioning.hpp
/usr/include/msgpack/vrefbuffer.h
/usr/include/msgpack/vrefbuffer.hpp
/usr/include/msgpack/vrefbuffer_decl.hpp
/usr/include/msgpack/x3_parse.hpp
/usr/include/msgpack/x3_parse_decl.hpp
/usr/include/msgpack/x3_unpack.hpp
/usr/include/msgpack/x3_unpack_decl.hpp
/usr/include/msgpack/zbuffer.h
/usr/include/msgpack/zbuffer.hpp
/usr/include/msgpack/zbuffer_decl.hpp
/usr/include/msgpack/zone.h
/usr/include/msgpack/zone.hpp
/usr/include/msgpack/zone_decl.hpp
/usr/lib64/cmake/msgpack/msgpack-config-version.cmake
/usr/lib64/cmake/msgpack/msgpack-config.cmake
/usr/lib64/cmake/msgpack/msgpack-targets-relwithdebinfo.cmake
/usr/lib64/cmake/msgpack/msgpack-targets.cmake
/usr/lib64/libmsgpackc.so
/usr/lib64/pkgconfig/msgpack.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmsgpackc.so.2
/usr/lib64/libmsgpackc.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/msgpack-c/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
