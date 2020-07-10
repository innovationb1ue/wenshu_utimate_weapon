function _$0c() {
    var _$i$ = _$Ks(_$T_(21) + _$HW._$H4); // the array + fixed postfix in indexjs
    _$SO(4096, _$i$.length !== 32);
    return _$4_(_$i$); // encrypt the array
}

// call on result of upper function
function _$az(_$28) {
    var _$i$ = _$28[_$oQ[1]](0);
    if (_$i$.length < 5) {
        return;
    }
    var _$Na = _$i$.pop();
    var _$DH = 0
        , _$tz = _$i$.length;
    while (_$DH < _$tz) {
        _$i$[_$DH++] ^= _$Na;
    }
    var _$qX = _$i$.length - 4;
    var _$hn = _$uE() - _$XB(_$i$[_$oQ[1]](_$qX))[0];
    _$i$ = _$i$[_$oQ[1]](0, _$qX);
    var _$IY = _$C$.Math[_$oQ[5]](_$C$[_$oQ[78]].log(_$hn / 1.164 + 1));
    var _$V8 = _$i$.length;
    var _$01 = [0, _$HW._$By][_$r2];
    _$DH = 0;
    while (_$DH < _$V8) {
        _$i$[_$DH] = _$IY | (_$i$[_$DH++] ^ _$01);
    }
    _$1V(8, _$IY);
    return _$i$;
}

// call on result of upper function
var _$Na = _$UJ(708, _$i$);