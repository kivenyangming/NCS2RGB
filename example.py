__all__ = ['example']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['emptyObject', 'hueToRgb', 'isHex', 'toHex', 'hwbToRgb', 'toColorObject', 'getColorArr', 'colorObject', 'rgbToHwb', 'cmykToRgb', 'ncolToRgb', 'w3trim', 'roundDecimals', 'rgbToCmyk', 'hslToRgb', 'ncsToRgb', 'rgbToHsl', 'hueToNcol', 'cl'])
@Js
def PyJsHoisted_toColorObject_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['hue', 'colorhexs', 'match', 'i', 'sat', 'arrlength', 'colornames', 'rgb', 'arr', 'x', 'c', 'y', 'opacity', 'typ', 'a'])
    var.put('arr', Js([]))
    var.put('colornames', Js([]))
    var.put('colorhexs', Js([]))
    var.put('c', var.get('w3trim')(var.get('c').callprop('toLowerCase')))
    var.put('x', var.get('c').callprop('substr', Js(0.0), Js(1.0)).callprop('toUpperCase'))
    var.put('y', var.get('c').callprop('substr', Js(1.0)))
    var.put('a', Js(1.0))
    if ((((((((var.get('x')==Js('R')) or (var.get('x')==Js('Y'))) or (var.get('x')==Js('G'))) or (var.get('x')==Js('C'))) or (var.get('x')==Js('B'))) or (var.get('x')==Js('M'))) or (var.get('x')==Js('W'))) and var.get('isNaN')(var.get('y')).neg()):
        if ((var.get('c').get('length')==Js(6.0)) and (var.get('c').callprop('indexOf', Js(','))==(-Js(1.0)))):
            pass
        else:
            var.put('c', ((Js('ncol(')+var.get('c'))+Js(')')))
    if (((var.get('c').get('length')!=Js(3.0)) and (var.get('c').get('length')!=Js(6.0))) and var.get('isNaN')(var.get('c')).neg()):
        var.put('c', ((Js('ncol(')+var.get('c'))+Js(')')))
    if ((var.get('c').callprop('indexOf', Js(','))>Js(0.0)) and (var.get('c').callprop('indexOf', Js('('))==(-Js(1.0)))):
        var.put('c', ((Js('ncol(')+var.get('c'))+Js(')')))
    if (((((var.get('c').callprop('substr', Js(0.0), Js(3.0))==Js('rgb')) or (var.get('c').callprop('substr', Js(0.0), Js(3.0))==Js('hsl'))) or (var.get('c').callprop('substr', Js(0.0), Js(3.0))==Js('hwb'))) or (var.get('c').callprop('substr', Js(0.0), Js(4.0))==Js('ncol'))) or (var.get('c').callprop('substr', Js(0.0), Js(4.0))==Js('cmyk'))):
        if (var.get('c').callprop('substr', Js(0.0), Js(4.0))==Js('ncol')):
            if ((var.get('c').callprop('split', Js(',')).get('length')==Js(4.0)) and (var.get('c').callprop('indexOf', Js('ncola'))==(-Js(1.0)))):
                var.put('c', var.get('c').callprop('replace', Js('ncol'), Js('ncola')))
            var.put('typ', Js('ncol'))
            var.put('c', var.get('c').callprop('substr', Js(4.0)))
        else:
            if (var.get('c').callprop('substr', Js(0.0), Js(4.0))==Js('cmyk')):
                var.put('typ', Js('cmyk'))
                var.put('c', var.get('c').callprop('substr', Js(4.0)))
            else:
                var.put('typ', var.get('c').callprop('substr', Js(0.0), Js(3.0)))
                var.put('c', var.get('c').callprop('substr', Js(3.0)))
        var.put('arrlength', Js(3.0))
        var.put('opacity', Js(False))
        if (var.get('c').callprop('substr', Js(0.0), Js(1.0)).callprop('toLowerCase')==Js('a')):
            var.put('arrlength', Js(4.0))
            var.put('opacity', Js(True))
            var.put('c', var.get('c').callprop('substr', Js(1.0)))
        else:
            if (var.get('typ')==Js('cmyk')):
                var.put('arrlength', Js(4.0))
                if (var.get('c').callprop('split', Js(',')).get('length')==Js(5.0)):
                    var.put('arrlength', Js(5.0))
                    var.put('opacity', Js(True))
        var.put('c', var.get('c').callprop('replace', Js('('), Js('')))
        var.put('c', var.get('c').callprop('replace', Js(')'), Js('')))
        var.put('arr', var.get('c').callprop('split', Js(',')))
        if (var.get('typ')==Js('rgb')):
            if (var.get('arr').get('length')!=var.get('arrlength')):
                return var.get('emptyObject')()
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('arrlength')):
                try:
                    if ((var.get('arr').get(var.get('i'))==Js('')) or (var.get('arr').get(var.get('i'))==Js(' '))):
                        var.get('arr').put(var.get('i'), Js('0'))
                    if (var.get('arr').get(var.get('i')).callprop('indexOf', Js('%'))>(-Js(1.0))):
                        var.get('arr').put(var.get('i'), var.get('arr').get(var.get('i')).callprop('replace', Js('%'), Js('')))
                        var.get('arr').put(var.get('i'), var.get('Number')((var.get('arr').get(var.get('i'))/Js(100.0))))
                        if (var.get('i')<Js(3.0)):
                            var.get('arr').put(var.get('i'), var.get('Math').callprop('round', (var.get('arr').get(var.get('i'))*Js(255.0))))
                    if var.get('isNaN')(var.get('arr').get(var.get('i'))):
                        return var.get('emptyObject')()
                    if (var.get('parseInt')(var.get('arr').get(var.get('i')))>Js(255.0)):
                        var.get('arr').put(var.get('i'), Js(255.0))
                    if (var.get('i')<Js(3.0)):
                        var.get('arr').put(var.get('i'), var.get('parseInt')(var.get('arr').get(var.get('i'))))
                    if ((var.get('i')==Js(3.0)) and (var.get('Number')(var.get('arr').get(var.get('i')))>Js(1.0))):
                        var.get('arr').put(var.get('i'), Js(1.0))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rgb', Js({'r':var.get('arr').get('0'),'g':var.get('arr').get('1'),'b':var.get('arr').get('2')}))
            if (var.get('opacity')==Js(True)):
                var.put('a', var.get('Number')(var.get('arr').get('3')))
        if (((var.get('typ')==Js('hsl')) or (var.get('typ')==Js('hwb'))) or (var.get('typ')==Js('ncol'))):
            while (var.get('arr').get('length')<var.get('arrlength')):
                var.get('arr').callprop('push', Js('0'))
            if ((var.get('typ')==Js('hsl')) or (var.get('typ')==Js('hwb'))):
                if (var.get('parseInt')(var.get('arr').get('0'))>=Js(360.0)):
                    var.get('arr').put('0', Js(0.0))
            #for JS loop
            var.put('i', Js(1.0))
            while (var.get('i')<var.get('arrlength')):
                try:
                    if (var.get('arr').get(var.get('i')).callprop('indexOf', Js('%'))>(-Js(1.0))):
                        var.get('arr').put(var.get('i'), var.get('arr').get(var.get('i')).callprop('replace', Js('%'), Js('')))
                        var.get('arr').put(var.get('i'), var.get('Number')(var.get('arr').get(var.get('i'))))
                        if var.get('isNaN')(var.get('arr').get(var.get('i'))):
                            return var.get('emptyObject')()
                        var.get('arr').put(var.get('i'), (var.get('arr').get(var.get('i'))/Js(100.0)))
                    else:
                        var.get('arr').put(var.get('i'), var.get('Number')(var.get('arr').get(var.get('i'))))
                    if (var.get('Number')(var.get('arr').get(var.get('i')))>Js(1.0)):
                        var.get('arr').put(var.get('i'), Js(1.0))
                    if (var.get('Number')(var.get('arr').get(var.get('i')))<Js(0.0)):
                        var.get('arr').put(var.get('i'), Js(0.0))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if (var.get('typ')==Js('hsl')):
                var.put('rgb', var.get('hslToRgb')(var.get('arr').get('0'), var.get('arr').get('1'), var.get('arr').get('2')))
                var.put('hue', var.get('Number')(var.get('arr').get('0')))
                var.put('sat', var.get('Number')(var.get('arr').get('1')))
            if (var.get('typ')==Js('hwb')):
                var.put('rgb', var.get('hwbToRgb')(var.get('arr').get('0'), var.get('arr').get('1'), var.get('arr').get('2')))
            if (var.get('typ')==Js('ncol')):
                var.put('rgb', var.get('ncolToRgb')(var.get('arr').get('0'), var.get('arr').get('1'), var.get('arr').get('2')))
            if (var.get('opacity')==Js(True)):
                var.put('a', var.get('Number')(var.get('arr').get('3')))
        if (var.get('typ')==Js('cmyk')):
            while (var.get('arr').get('length')<var.get('arrlength')):
                var.get('arr').callprop('push', Js('0'))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('arrlength')):
                try:
                    if (var.get('arr').get(var.get('i')).callprop('indexOf', Js('%'))>(-Js(1.0))):
                        var.get('arr').put(var.get('i'), var.get('arr').get(var.get('i')).callprop('replace', Js('%'), Js('')))
                        var.get('arr').put(var.get('i'), var.get('Number')(var.get('arr').get(var.get('i'))))
                        if var.get('isNaN')(var.get('arr').get(var.get('i'))):
                            return var.get('emptyObject')()
                        var.get('arr').put(var.get('i'), (var.get('arr').get(var.get('i'))/Js(100.0)))
                    else:
                        var.get('arr').put(var.get('i'), var.get('Number')(var.get('arr').get(var.get('i'))))
                    if (var.get('Number')(var.get('arr').get(var.get('i')))>Js(1.0)):
                        var.get('arr').put(var.get('i'), Js(1.0))
                    if (var.get('Number')(var.get('arr').get(var.get('i')))<Js(0.0)):
                        var.get('arr').put(var.get('i'), Js(0.0))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('rgb', var.get('cmykToRgb')(var.get('arr').get('0'), var.get('arr').get('1'), var.get('arr').get('2'), var.get('arr').get('3')))
            if (var.get('opacity')==Js(True)):
                var.put('a', var.get('Number')(var.get('arr').get('4')))
    else:
        if (var.get('c').callprop('substr', Js(0.0), Js(3.0))==Js('ncs')):
            var.put('rgb', var.get('ncsToRgb')(var.get('c')))
        else:
            var.put('match', Js(False))
            var.put('colornames', var.get('getColorArr')(Js('names')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('colornames').get('length')):
                try:
                    if (var.get('c').callprop('toLowerCase')==var.get('colornames').get(var.get('i')).callprop('toLowerCase')):
                        var.put('colorhexs', var.get('getColorArr')(Js('hexs')))
                        var.put('match', Js(True))
                        var.put('rgb', Js({'r':var.get('parseInt')(var.get('colorhexs').get(var.get('i')).callprop('substr', Js(0.0), Js(2.0)), Js(16.0)),'g':var.get('parseInt')(var.get('colorhexs').get(var.get('i')).callprop('substr', Js(2.0), Js(2.0)), Js(16.0)),'b':var.get('parseInt')(var.get('colorhexs').get(var.get('i')).callprop('substr', Js(4.0), Js(2.0)), Js(16.0))}))
                        break
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if (var.get('match')==Js(False)):
                var.put('c', var.get('c').callprop('replace', Js('#'), Js('')))
                if (var.get('c').get('length')==Js(3.0)):
                    var.put('c', (((((var.get('c').callprop('substr', Js(0.0), Js(1.0))+var.get('c').callprop('substr', Js(0.0), Js(1.0)))+var.get('c').callprop('substr', Js(1.0), Js(1.0)))+var.get('c').callprop('substr', Js(1.0), Js(1.0)))+var.get('c').callprop('substr', Js(2.0), Js(1.0)))+var.get('c').callprop('substr', Js(2.0), Js(1.0))))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('c').get('length')):
                    try:
                        if var.get('isHex')(var.get('c').callprop('substr', var.get('i'), Js(1.0))).neg():
                            return var.get('emptyObject')()
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                var.get('arr').put('0', var.get('parseInt')(var.get('c').callprop('substr', Js(0.0), Js(2.0)), Js(16.0)))
                var.get('arr').put('1', var.get('parseInt')(var.get('c').callprop('substr', Js(2.0), Js(2.0)), Js(16.0)))
                var.get('arr').put('2', var.get('parseInt')(var.get('c').callprop('substr', Js(4.0), Js(2.0)), Js(16.0)))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<Js(3.0)):
                    try:
                        if var.get('isNaN')(var.get('arr').get(var.get('i'))):
                            return var.get('emptyObject')()
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                var.put('rgb', Js({'r':var.get('arr').get('0'),'g':var.get('arr').get('1'),'b':var.get('arr').get('2')}))
    return var.get('colorObject')(var.get('rgb'), var.get('a'), var.get('hue'), var.get('sat'))
PyJsHoisted_toColorObject_.func_name = 'toColorObject'
var.put('toColorObject', PyJsHoisted_toColorObject_)
@Js
def PyJsHoisted_colorObject_(rgb, a, h, s, this, arguments, var=var):
    var = Scope({'rgb':rgb, 'a':a, 'h':h, 's':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['s', 'h', 'sat', 'color', 'a', 'rgb', 'cmyk', 'hue', 'hsl', 'hwb', 'ncol'])
    pass
    if var.get('rgb').neg():
        return var.get('emptyObject')()
    if PyJsStrictEq(var.get('a'),var.get(u"null")):
        var.put('a', Js(1.0))
    var.put('hsl', var.get('rgbToHsl')(var.get('rgb').get('r'), var.get('rgb').get('g'), var.get('rgb').get('b')))
    var.put('hwb', var.get('rgbToHwb')(var.get('rgb').get('r'), var.get('rgb').get('g'), var.get('rgb').get('b')))
    var.put('cmyk', var.get('rgbToCmyk')(var.get('rgb').get('r'), var.get('rgb').get('g'), var.get('rgb').get('b')))
    var.put('hue', (var.get('h') or var.get('hsl').get('h')))
    var.put('sat', (var.get('s') or var.get('hsl').get('s')))
    var.put('ncol', var.get('hueToNcol')(var.get('hue')))
    def PyJs_LONG_0_(var=var):
        return var.put('color', Js({'red':var.get('rgb').get('r'),'green':var.get('rgb').get('g'),'blue':var.get('rgb').get('b'),'hue':var.get('hue'),'sat':var.get('sat'),'lightness':var.get('hsl').get('l'),'whiteness':var.get('hwb').get('w'),'blackness':var.get('hwb').get('b'),'cyan':var.get('cmyk').get('c'),'magenta':var.get('cmyk').get('m'),'yellow':var.get('cmyk').get('y'),'black':var.get('cmyk').get('k'),'ncol':var.get('ncol'),'opacity':var.get('a'),'valid':Js(True)}))
    PyJs_LONG_0_()
    var.put('color', var.get('roundDecimals')(var.get('color')))
    return var.get('color')
PyJsHoisted_colorObject_.func_name = 'colorObject'
var.put('colorObject', PyJsHoisted_colorObject_)
@Js
def PyJsHoisted_emptyObject_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return Js({'red':Js(0.0),'green':Js(0.0),'blue':Js(0.0),'hue':Js(0.0),'sat':Js(0.0),'lightness':Js(0.0),'whiteness':Js(0.0),'blackness':Js(0.0),'cyan':Js(0.0),'magenta':Js(0.0),'yellow':Js(0.0),'black':Js(0.0),'ncol':Js('R'),'opacity':Js(1.0),'valid':Js(False)})
PyJsHoisted_emptyObject_.func_name = 'emptyObject'
var.put('emptyObject', PyJsHoisted_emptyObject_)
@Js
def PyJsHoisted_getColorArr_(x, this, arguments, var=var):
    var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
    var.registers(['x'])
    if (var.get('x')==Js('names')):
        return Js([Js('AliceBlue'), Js('AntiqueWhite'), Js('Aqua'), Js('Aquamarine'), Js('Azure'), Js('Beige'), Js('Bisque'), Js('Black'), Js('BlanchedAlmond'), Js('Blue'), Js('BlueViolet'), Js('Brown'), Js('BurlyWood'), Js('CadetBlue'), Js('Chartreuse'), Js('Chocolate'), Js('Coral'), Js('CornflowerBlue'), Js('Cornsilk'), Js('Crimson'), Js('Cyan'), Js('DarkBlue'), Js('DarkCyan'), Js('DarkGoldenRod'), Js('DarkGray'), Js('DarkGrey'), Js('DarkGreen'), Js('DarkKhaki'), Js('DarkMagenta'), Js('DarkOliveGreen'), Js('DarkOrange'), Js('DarkOrchid'), Js('DarkRed'), Js('DarkSalmon'), Js('DarkSeaGreen'), Js('DarkSlateBlue'), Js('DarkSlateGray'), Js('DarkSlateGrey'), Js('DarkTurquoise'), Js('DarkViolet'), Js('DeepPink'), Js('DeepSkyBlue'), Js('DimGray'), Js('DimGrey'), Js('DodgerBlue'), Js('FireBrick'), Js('FloralWhite'), Js('ForestGreen'), Js('Fuchsia'), Js('Gainsboro'), Js('GhostWhite'), Js('Gold'), Js('GoldenRod'), Js('Gray'), Js('Grey'), Js('Green'), Js('GreenYellow'), Js('HoneyDew'), Js('HotPink'), Js('IndianRed'), Js('Indigo'), Js('Ivory'), Js('Khaki'), Js('Lavender'), Js('LavenderBlush'), Js('LawnGreen'), Js('LemonChiffon'), Js('LightBlue'), Js('LightCoral'), Js('LightCyan'), Js('LightGoldenRodYellow'), Js('LightGray'), Js('LightGrey'), Js('LightGreen'), Js('LightPink'), Js('LightSalmon'), Js('LightSeaGreen'), Js('LightSkyBlue'), Js('LightSlateGray'), Js('LightSlateGrey'), Js('LightSteelBlue'), Js('LightYellow'), Js('Lime'), Js('LimeGreen'), Js('Linen'), Js('Magenta'), Js('Maroon'), Js('MediumAquaMarine'), Js('MediumBlue'), Js('MediumOrchid'), Js('MediumPurple'), Js('MediumSeaGreen'), Js('MediumSlateBlue'), Js('MediumSpringGreen'), Js('MediumTurquoise'), Js('MediumVioletRed'), Js('MidnightBlue'), Js('MintCream'), Js('MistyRose'), Js('Moccasin'), Js('NavajoWhite'), Js('Navy'), Js('OldLace'), Js('Olive'), Js('OliveDrab'), Js('Orange'), Js('OrangeRed'), Js('Orchid'), Js('PaleGoldenRod'), Js('PaleGreen'), Js('PaleTurquoise'), Js('PaleVioletRed'), Js('PapayaWhip'), Js('PeachPuff'), Js('Peru'), Js('Pink'), Js('Plum'), Js('PowderBlue'), Js('Purple'), Js('RebeccaPurple'), Js('Red'), Js('RosyBrown'), Js('RoyalBlue'), Js('SaddleBrown'), Js('Salmon'), Js('SandyBrown'), Js('SeaGreen'), Js('SeaShell'), Js('Sienna'), Js('Silver'), Js('SkyBlue'), Js('SlateBlue'), Js('SlateGray'), Js('SlateGrey'), Js('Snow'), Js('SpringGreen'), Js('SteelBlue'), Js('Tan'), Js('Teal'), Js('Thistle'), Js('Tomato'), Js('Turquoise'), Js('Violet'), Js('Wheat'), Js('White'), Js('WhiteSmoke'), Js('Yellow'), Js('YellowGreen')])
    if (var.get('x')==Js('hexs')):
        return Js([Js('f0f8ff'), Js('faebd7'), Js('00ffff'), Js('7fffd4'), Js('f0ffff'), Js('f5f5dc'), Js('ffe4c4'), Js('000000'), Js('ffebcd'), Js('0000ff'), Js('8a2be2'), Js('a52a2a'), Js('deb887'), Js('5f9ea0'), Js('7fff00'), Js('d2691e'), Js('ff7f50'), Js('6495ed'), Js('fff8dc'), Js('dc143c'), Js('00ffff'), Js('00008b'), Js('008b8b'), Js('b8860b'), Js('a9a9a9'), Js('a9a9a9'), Js('006400'), Js('bdb76b'), Js('8b008b'), Js('556b2f'), Js('ff8c00'), Js('9932cc'), Js('8b0000'), Js('e9967a'), Js('8fbc8f'), Js('483d8b'), Js('2f4f4f'), Js('2f4f4f'), Js('00ced1'), Js('9400d3'), Js('ff1493'), Js('00bfff'), Js('696969'), Js('696969'), Js('1e90ff'), Js('b22222'), Js('fffaf0'), Js('228b22'), Js('ff00ff'), Js('dcdcdc'), Js('f8f8ff'), Js('ffd700'), Js('daa520'), Js('808080'), Js('808080'), Js('008000'), Js('adff2f'), Js('f0fff0'), Js('ff69b4'), Js('cd5c5c'), Js('4b0082'), Js('fffff0'), Js('f0e68c'), Js('e6e6fa'), Js('fff0f5'), Js('7cfc00'), Js('fffacd'), Js('add8e6'), Js('f08080'), Js('e0ffff'), Js('fafad2'), Js('d3d3d3'), Js('d3d3d3'), Js('90ee90'), Js('ffb6c1'), Js('ffa07a'), Js('20b2aa'), Js('87cefa'), Js('778899'), Js('778899'), Js('b0c4de'), Js('ffffe0'), Js('00ff00'), Js('32cd32'), Js('faf0e6'), Js('ff00ff'), Js('800000'), Js('66cdaa'), Js('0000cd'), Js('ba55d3'), Js('9370db'), Js('3cb371'), Js('7b68ee'), Js('00fa9a'), Js('48d1cc'), Js('c71585'), Js('191970'), Js('f5fffa'), Js('ffe4e1'), Js('ffe4b5'), Js('ffdead'), Js('000080'), Js('fdf5e6'), Js('808000'), Js('6b8e23'), Js('ffa500'), Js('ff4500'), Js('da70d6'), Js('eee8aa'), Js('98fb98'), Js('afeeee'), Js('db7093'), Js('ffefd5'), Js('ffdab9'), Js('cd853f'), Js('ffc0cb'), Js('dda0dd'), Js('b0e0e6'), Js('800080'), Js('663399'), Js('ff0000'), Js('bc8f8f'), Js('4169e1'), Js('8b4513'), Js('fa8072'), Js('f4a460'), Js('2e8b57'), Js('fff5ee'), Js('a0522d'), Js('c0c0c0'), Js('87ceeb'), Js('6a5acd'), Js('708090'), Js('708090'), Js('fffafa'), Js('00ff7f'), Js('4682b4'), Js('d2b48c'), Js('008080'), Js('d8bfd8'), Js('ff6347'), Js('40e0d0'), Js('ee82ee'), Js('f5deb3'), Js('ffffff'), Js('f5f5f5'), Js('ffff00'), Js('9acd32')])
PyJsHoisted_getColorArr_.func_name = 'getColorArr'
var.put('getColorArr', PyJsHoisted_getColorArr_)
@Js
def PyJsHoisted_roundDecimals_(c, this, arguments, var=var):
    var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c'])
    var.get('c').put('red', var.get('Number')(var.get('c').get('red').callprop('toFixed', Js(0.0))))
    var.get('c').put('green', var.get('Number')(var.get('c').get('green').callprop('toFixed', Js(0.0))))
    var.get('c').put('blue', var.get('Number')(var.get('c').get('blue').callprop('toFixed', Js(0.0))))
    var.get('c').put('hue', var.get('Number')(var.get('c').get('hue').callprop('toFixed', Js(0.0))))
    var.get('c').put('sat', var.get('Number')(var.get('c').get('sat').callprop('toFixed', Js(2.0))))
    var.get('c').put('lightness', var.get('Number')(var.get('c').get('lightness').callprop('toFixed', Js(2.0))))
    var.get('c').put('whiteness', var.get('Number')(var.get('c').get('whiteness').callprop('toFixed', Js(2.0))))
    var.get('c').put('blackness', var.get('Number')(var.get('c').get('blackness').callprop('toFixed', Js(2.0))))
    var.get('c').put('cyan', var.get('Number')(var.get('c').get('cyan').callprop('toFixed', Js(2.0))))
    var.get('c').put('magenta', var.get('Number')(var.get('c').get('magenta').callprop('toFixed', Js(2.0))))
    var.get('c').put('yellow', var.get('Number')(var.get('c').get('yellow').callprop('toFixed', Js(2.0))))
    var.get('c').put('black', var.get('Number')(var.get('c').get('black').callprop('toFixed', Js(2.0))))
    var.get('c').put('ncol', (var.get('c').get('ncol').callprop('substr', Js(0.0), Js(1.0))+var.get('Math').callprop('round', var.get('Number')(var.get('c').get('ncol').callprop('substr', Js(1.0))))))
    var.get('c').put('opacity', var.get('Number')(var.get('c').get('opacity').callprop('toFixed', Js(2.0))))
    return var.get('c')
PyJsHoisted_roundDecimals_.func_name = 'roundDecimals'
var.put('roundDecimals', PyJsHoisted_roundDecimals_)
@Js
def PyJsHoisted_hslToRgb_(hue, sat, light, this, arguments, var=var):
    var = Scope({'hue':hue, 'sat':sat, 'light':light, 'this':this, 'arguments':arguments}, var)
    var.registers(['r', 't1', 't2', 'g', 'sat', 'light', 'b', 'hue'])
    pass
    var.put('hue', (var.get('hue')/Js(60.0)))
    if (var.get('light')<=Js(0.5)):
        var.put('t2', (var.get('light')*(var.get('sat')+Js(1.0))))
    else:
        var.put('t2', ((var.get('light')+var.get('sat'))-(var.get('light')*var.get('sat'))))
    var.put('t1', ((var.get('light')*Js(2.0))-var.get('t2')))
    var.put('r', (var.get('hueToRgb')(var.get('t1'), var.get('t2'), (var.get('hue')+Js(2.0)))*Js(255.0)))
    var.put('g', (var.get('hueToRgb')(var.get('t1'), var.get('t2'), var.get('hue'))*Js(255.0)))
    var.put('b', (var.get('hueToRgb')(var.get('t1'), var.get('t2'), (var.get('hue')-Js(2.0)))*Js(255.0)))
    return Js({'r':var.get('r'),'g':var.get('g'),'b':var.get('b')})
PyJsHoisted_hslToRgb_.func_name = 'hslToRgb'
var.put('hslToRgb', PyJsHoisted_hslToRgb_)
@Js
def PyJsHoisted_hueToRgb_(t1, t2, hue, this, arguments, var=var):
    var = Scope({'t1':t1, 't2':t2, 'hue':hue, 'this':this, 'arguments':arguments}, var)
    var.registers(['t1', 'hue', 't2'])
    if (var.get('hue')<Js(0.0)):
        var.put('hue', Js(6.0), '+')
    if (var.get('hue')>=Js(6.0)):
        var.put('hue', Js(6.0), '-')
    if (var.get('hue')<Js(1.0)):
        return (((var.get('t2')-var.get('t1'))*var.get('hue'))+var.get('t1'))
    else:
        if (var.get('hue')<Js(3.0)):
            return var.get('t2')
        else:
            if (var.get('hue')<Js(4.0)):
                return (((var.get('t2')-var.get('t1'))*(Js(4.0)-var.get('hue')))+var.get('t1'))
            else:
                return var.get('t1')
PyJsHoisted_hueToRgb_.func_name = 'hueToRgb'
var.put('hueToRgb', PyJsHoisted_hueToRgb_)
@Js
def PyJsHoisted_hwbToRgb_(hue, white, black, this, arguments, var=var):
    var = Scope({'hue':hue, 'white':white, 'black':black, 'this':this, 'arguments':arguments}, var)
    var.registers(['tot', 'black', 'rgbArr', 'rgb', 'hue', 'i', 'white'])
    var.put('rgbArr', Js([]))
    var.put('rgb', var.get('hslToRgb')(var.get('hue'), Js(1.0), Js(0.5)))
    var.get('rgbArr').put('0', (var.get('rgb').get('r')/Js(255.0)))
    var.get('rgbArr').put('1', (var.get('rgb').get('g')/Js(255.0)))
    var.get('rgbArr').put('2', (var.get('rgb').get('b')/Js(255.0)))
    var.put('tot', (var.get('white')+var.get('black')))
    if (var.get('tot')>Js(1.0)):
        var.put('white', var.get('Number')((var.get('white')/var.get('tot')).callprop('toFixed', Js(2.0))))
        var.put('black', var.get('Number')((var.get('black')/var.get('tot')).callprop('toFixed', Js(2.0))))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(3.0)):
        try:
            var.get('rgbArr').put(var.get('i'), ((Js(1.0)-var.get('white'))-var.get('black')), '*')
            var.get('rgbArr').put(var.get('i'), var.get('white'), '+')
            var.get('rgbArr').put(var.get('i'), var.get('Number')((var.get('rgbArr').get(var.get('i'))*Js(255.0))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return Js({'r':var.get('rgbArr').get('0'),'g':var.get('rgbArr').get('1'),'b':var.get('rgbArr').get('2')})
PyJsHoisted_hwbToRgb_.func_name = 'hwbToRgb'
var.put('hwbToRgb', PyJsHoisted_hwbToRgb_)
@Js
def PyJsHoisted_cmykToRgb_(c, m, y, k, this, arguments, var=var):
    var = Scope({'c':c, 'm':m, 'y':y, 'k':k, 'this':this, 'arguments':arguments}, var)
    var.registers(['r', 'g', 'm', 'c', 'b', 'y', 'k'])
    pass
    var.put('r', (Js(255.0)-(var.get('Math').callprop('min', Js(1.0), ((var.get('c')*(Js(1.0)-var.get('k')))+var.get('k')))*Js(255.0))))
    var.put('g', (Js(255.0)-(var.get('Math').callprop('min', Js(1.0), ((var.get('m')*(Js(1.0)-var.get('k')))+var.get('k')))*Js(255.0))))
    var.put('b', (Js(255.0)-(var.get('Math').callprop('min', Js(1.0), ((var.get('y')*(Js(1.0)-var.get('k')))+var.get('k')))*Js(255.0))))
    return Js({'r':var.get('r'),'g':var.get('g'),'b':var.get('b')})
PyJsHoisted_cmykToRgb_.func_name = 'cmykToRgb'
var.put('cmykToRgb', PyJsHoisted_cmykToRgb_)
@Js
def PyJsHoisted_ncolToRgb_(ncol, white, black, this, arguments, var=var):
    var = Scope({'ncol':ncol, 'white':white, 'black':black, 'this':this, 'arguments':arguments}, var)
    var.registers(['white', 'h', 'percent', 'black', 'w', 'letter', 'b', 'ncol'])
    pass
    var.put('h', var.get('ncol'))
    if var.get('isNaN')(var.get('ncol').callprop('substr', Js(0.0), Js(1.0))):
        var.put('letter', var.get('ncol').callprop('substr', Js(0.0), Js(1.0)).callprop('toUpperCase'))
        var.put('percent', var.get('ncol').callprop('substr', Js(1.0)))
        if (var.get('percent')==Js('')):
            var.put('percent', Js(0.0))
        var.put('percent', var.get('Number')(var.get('percent')))
        if var.get('isNaN')(var.get('percent')):
            return Js(False)
        if (var.get('letter')==Js('R')):
            var.put('h', (Js(0.0)+(var.get('percent')*Js(0.6))))
        if (var.get('letter')==Js('Y')):
            var.put('h', (Js(60.0)+(var.get('percent')*Js(0.6))))
        if (var.get('letter')==Js('G')):
            var.put('h', (Js(120.0)+(var.get('percent')*Js(0.6))))
        if (var.get('letter')==Js('C')):
            var.put('h', (Js(180.0)+(var.get('percent')*Js(0.6))))
        if (var.get('letter')==Js('B')):
            var.put('h', (Js(240.0)+(var.get('percent')*Js(0.6))))
        if (var.get('letter')==Js('M')):
            var.put('h', (Js(300.0)+(var.get('percent')*Js(0.6))))
        if (var.get('letter')==Js('W')):
            var.put('h', Js(0.0))
            var.put('white', (Js(1.0)-(var.get('percent')/Js(100.0))))
            var.put('black', (var.get('percent')/Js(100.0)))
    return var.get('hwbToRgb')(var.get('h'), var.get('white'), var.get('black'))
PyJsHoisted_ncolToRgb_.func_name = 'ncolToRgb'
var.put('ncolToRgb', PyJsHoisted_ncolToRgb_)
@Js
def PyJsHoisted_hueToNcol_(hue, this, arguments, var=var):
    var = Scope({'hue':hue, 'this':this, 'arguments':arguments}, var)
    var.registers(['hue'])
    while (var.get('hue')>=Js(360.0)):
        var.put('hue', (var.get('hue')-Js(360.0)))
    if (var.get('hue')<Js(60.0)):
        return (Js('R')+(var.get('hue')/Js(0.6)))
    if (var.get('hue')<Js(120.0)):
        return (Js('Y')+((var.get('hue')-Js(60.0))/Js(0.6)))
    if (var.get('hue')<Js(180.0)):
        return (Js('G')+((var.get('hue')-Js(120.0))/Js(0.6)))
    if (var.get('hue')<Js(240.0)):
        return (Js('C')+((var.get('hue')-Js(180.0))/Js(0.6)))
    if (var.get('hue')<Js(300.0)):
        return (Js('B')+((var.get('hue')-Js(240.0))/Js(0.6)))
    if (var.get('hue')<Js(360.0)):
        return (Js('M')+((var.get('hue')-Js(300.0))/Js(0.6)))
PyJsHoisted_hueToNcol_.func_name = 'hueToNcol'
var.put('hueToNcol', PyJsHoisted_hueToNcol_)
@Js
def PyJsHoisted_ncsToRgb_(ncs, this, arguments, var=var):
    var = Scope({'ncs':ncs, 'this':this, 'arguments':arguments}, var)
    var.registers(['max', 'grey', 'chroma1', 'chroma', 'r', 'factor2', 'red1', 'b', 'green2', 'bc', 'red2', 'ncs', 'g', 'percent', 'blue1', 'black', 'black1', 'blue2', 'factor1'])
    pass
    var.put('ncs', var.get('w3trim')(var.get('ncs')).callprop('toUpperCase'))
    var.put('ncs', var.get('ncs').callprop('replace', Js('('), Js('')))
    var.put('ncs', var.get('ncs').callprop('replace', Js(')'), Js('')))
    var.put('ncs', var.get('ncs').callprop('replace', Js('NCS'), Js('NCS ')))
    var.put('ncs', var.get('ncs').callprop('replace', JsRegExp('/  /g'), Js(' ')))
    if (var.get('ncs').callprop('indexOf', Js('NCS'))==(-Js(1.0))):
        var.put('ncs', (Js('NCS ')+var.get('ncs')))
    var.put('ncs', var.get('ncs').callprop('match', JsRegExp('/^(?:NCS|NCS\\sS)\\s(\\d{2})(\\d{2})-(N|[A-Z])(\\d{2})?([A-Z])?$/')))
    if PyJsStrictEq(var.get('ncs'),var.get(u"null")):
        return Js(False)
    var.put('black', var.get('parseInt')(var.get('ncs').get('1'), Js(10.0)))
    var.put('chroma', var.get('parseInt')(var.get('ncs').get('2'), Js(10.0)))
    var.put('bc', var.get('ncs').get('3'))
    if (((((var.get('bc')!=Js('N')) and (var.get('bc')!=Js('Y'))) and (var.get('bc')!=Js('R'))) and (var.get('bc')!=Js('B'))) and (var.get('bc')!=Js('G'))):
        return Js(False)
    var.put('percent', (var.get('parseInt')(var.get('ncs').get('4'), Js(10.0)) or Js(0.0)))
    if PyJsStrictNeq(var.get('bc'),Js('N')):
        var.put('black1', ((Js(1.05)*var.get('black'))-Js(5.25)))
        var.put('chroma1', var.get('chroma'))
        if (PyJsStrictEq(var.get('bc'),Js('Y')) and (var.get('percent')<=Js(60.0))):
            var.put('red1', Js(1.0))
        else:
            if ((PyJsStrictEq(var.get('bc'),Js('Y')) and (var.get('percent')>Js(60.0))) or (PyJsStrictEq(var.get('bc'),Js('R')) and (var.get('percent')<=Js(80.0)))):
                if PyJsStrictEq(var.get('bc'),Js('Y')):
                    var.put('factor1', (var.get('percent')-Js(60.0)))
                else:
                    var.put('factor1', (var.get('percent')+Js(40.0)))
                var.put('red1', ((var.get('Math').callprop('sqrt', (Js(14884.0)-var.get('Math').callprop('pow', var.get('factor1'), Js(2.0))))-Js(22.0))/Js(100.0)))
            else:
                if ((PyJsStrictEq(var.get('bc'),Js('R')) and (var.get('percent')>Js(80.0))) or PyJsStrictEq(var.get('bc'),Js('B'))):
                    var.put('red1', Js(0.0))
                else:
                    if PyJsStrictEq(var.get('bc'),Js('G')):
                        var.put('factor1', (var.get('percent')-Js(170.0)))
                        var.put('red1', ((var.get('Math').callprop('sqrt', (Js(33800.0)-var.get('Math').callprop('pow', var.get('factor1'), Js(2.0))))-Js(70.0))/Js(100.0)))
        if (PyJsStrictEq(var.get('bc'),Js('Y')) and (var.get('percent')<=Js(80.0))):
            var.put('blue1', Js(0.0))
        else:
            if ((PyJsStrictEq(var.get('bc'),Js('Y')) and (var.get('percent')>Js(80.0))) or (PyJsStrictEq(var.get('bc'),Js('R')) and (var.get('percent')<=Js(60.0)))):
                if PyJsStrictEq(var.get('bc'),Js('Y')):
                    var.put('factor1', ((var.get('percent')-Js(80.0))+Js(20.5)))
                else:
                    var.put('factor1', ((var.get('percent')+Js(20.0))+Js(20.5)))
                var.put('blue1', ((Js(104.0)-var.get('Math').callprop('sqrt', (Js(11236.0)-var.get('Math').callprop('pow', var.get('factor1'), Js(2.0)))))/Js(100.0)))
            else:
                if ((PyJsStrictEq(var.get('bc'),Js('R')) and (var.get('percent')>Js(60.0))) or (PyJsStrictEq(var.get('bc'),Js('B')) and (var.get('percent')<=Js(80.0)))):
                    if PyJsStrictEq(var.get('bc'),Js('R')):
                        var.put('factor1', ((var.get('percent')-Js(60.0))-Js(60.0)))
                    else:
                        var.put('factor1', ((var.get('percent')+Js(40.0))-Js(60.0)))
                    var.put('blue1', ((var.get('Math').callprop('sqrt', (Js(10000.0)-var.get('Math').callprop('pow', var.get('factor1'), Js(2.0))))-Js(10.0))/Js(100.0)))
                else:
                    if ((PyJsStrictEq(var.get('bc'),Js('B')) and (var.get('percent')>Js(80.0))) or (PyJsStrictEq(var.get('bc'),Js('G')) and (var.get('percent')<=Js(40.0)))):
                        if PyJsStrictEq(var.get('bc'),Js('B')):
                            var.put('factor1', ((var.get('percent')-Js(80.0))-Js(131.0)))
                        else:
                            var.put('factor1', ((var.get('percent')+Js(20.0))-Js(131.0)))
                        var.put('blue1', ((Js(122.0)-var.get('Math').callprop('sqrt', (Js(19881.0)-var.get('Math').callprop('pow', var.get('factor1'), Js(2.0)))))/Js(100.0)))
                    else:
                        if (PyJsStrictEq(var.get('bc'),Js('G')) and (var.get('percent')>Js(40.0))):
                            var.put('blue1', Js(0.0))
        if PyJsStrictEq(var.get('bc'),Js('Y')):
            var.put('green1', ((Js(85.0)-((Js(17.0)/Js(20.0))*var.get('percent')))/Js(100.0)))
        else:
            if (PyJsStrictEq(var.get('bc'),Js('R')) and (var.get('percent')<=Js(60.0))):
                var.put('green1', Js(0.0))
            else:
                if (PyJsStrictEq(var.get('bc'),Js('R')) and (var.get('percent')>Js(60.0))):
                    var.put('factor1', ((var.get('percent')-Js(60.0))+Js(35.0)))
                    var.put('green1', ((Js(67.5)-var.get('Math').callprop('sqrt', (Js(5776.0)-var.get('Math').callprop('pow', var.get('factor1'), Js(2.0)))))/Js(100.0)))
                else:
                    if (PyJsStrictEq(var.get('bc'),Js('B')) and (var.get('percent')<=Js(60.0))):
                        var.put('factor1', ((Js(1.0)*var.get('percent'))-Js(68.5)))
                        var.put('green1', ((Js(6.5)+var.get('Math').callprop('sqrt', (Js(7044.5)-var.get('Math').callprop('pow', var.get('factor1'), Js(2.0)))))/Js(100.0)))
                    else:
                        if ((PyJsStrictEq(var.get('bc'),Js('B')) and (var.get('percent')>Js(60.0))) or (PyJsStrictEq(var.get('bc'),Js('G')) and (var.get('percent')<=Js(60.0)))):
                            var.put('green1', Js(0.9))
                        else:
                            if (PyJsStrictEq(var.get('bc'),Js('G')) and (var.get('percent')>Js(60.0))):
                                var.put('factor1', (var.get('percent')-Js(60.0)))
                                var.put('green1', ((Js(90.0)-((Js(1.0)/Js(8.0))*var.get('factor1')))/Js(100.0)))
        var.put('factor1', (((var.get('red1')+var.get('green1'))+var.get('blue1'))/Js(3.0)))
        var.put('red2', ((((var.get('factor1')-var.get('red1'))*(Js(100.0)-var.get('chroma1')))/Js(100.0))+var.get('red1')))
        var.put('green2', ((((var.get('factor1')-var.get('green1'))*(Js(100.0)-var.get('chroma1')))/Js(100.0))+var.get('green1')))
        var.put('blue2', ((((var.get('factor1')-var.get('blue1'))*(Js(100.0)-var.get('chroma1')))/Js(100.0))+var.get('blue1')))
        if ((var.get('red2')>var.get('green2')) and (var.get('red2')>var.get('blue2'))):
            var.put('max', var.get('red2'))
        else:
            if ((var.get('green2')>var.get('red2')) and (var.get('green2')>var.get('blue2'))):
                var.put('max', var.get('green2'))
            else:
                if ((var.get('blue2')>var.get('red2')) and (var.get('blue2')>var.get('green2'))):
                    var.put('max', var.get('blue2'))
                else:
                    var.put('max', (((var.get('red2')+var.get('green2'))+var.get('blue2'))/Js(3.0)))
        var.put('factor2', (Js(1.0)/var.get('max')))
        var.put('r', var.get('parseInt')(((((var.get('red2')*var.get('factor2'))*(Js(100.0)-var.get('black1')))/Js(100.0))*Js(255.0)), Js(10.0)))
        var.put('g', var.get('parseInt')(((((var.get('green2')*var.get('factor2'))*(Js(100.0)-var.get('black1')))/Js(100.0))*Js(255.0)), Js(10.0)))
        var.put('b', var.get('parseInt')(((((var.get('blue2')*var.get('factor2'))*(Js(100.0)-var.get('black1')))/Js(100.0))*Js(255.0)), Js(10.0)))
        if (var.get('r')>Js(255.0)):
            var.put('r', Js(255.0))
        if (var.get('g')>Js(255.0)):
            var.put('g', Js(255.0))
        if (var.get('b')>Js(255.0)):
            var.put('b', Js(255.0))
        if (var.get('r')<Js(0.0)):
            var.put('r', Js(0.0))
        if (var.get('g')<Js(0.0)):
            var.put('g', Js(0.0))
        if (var.get('b')<Js(0.0)):
            var.put('b', Js(0.0))
    else:
        var.put('grey', var.get('parseInt')(((Js(1.0)-(var.get('black')/Js(100.0)))*Js(255.0)), Js(10.0)))
        if (var.get('grey')>Js(255.0)):
            var.put('grey', Js(255.0))
        if (var.get('grey')<Js(0.0)):
            var.put('grey', Js(0.0))
        var.put('r', var.get('grey'))
        var.put('g', var.get('grey'))
        var.put('b', var.get('grey'))
    return Js({'r':var.get('r'),'g':var.get('g'),'b':var.get('b')})
PyJsHoisted_ncsToRgb_.func_name = 'ncsToRgb'
var.put('ncsToRgb', PyJsHoisted_ncsToRgb_)
@Js
def PyJsHoisted_rgbToHsl_(r, g, b, this, arguments, var=var):
    var = Scope({'r':r, 'g':g, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['r', 'max', 'g', 'maxcolor', 's', 'b', 'h', 'rgb', 'min', 'l', 'i'])
    var.put('rgb', Js([]))
    var.get('rgb').put('0', (var.get('r')/Js(255.0)))
    var.get('rgb').put('1', (var.get('g')/Js(255.0)))
    var.get('rgb').put('2', (var.get('b')/Js(255.0)))
    var.put('min', var.get('rgb').get('0'))
    var.put('max', var.get('rgb').get('0'))
    var.put('maxcolor', Js(0.0))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('rgb').get('length')-Js(1.0))):
        try:
            if (var.get('rgb').get((var.get('i')+Js(1.0)))<=var.get('min')):
                var.put('min', var.get('rgb').get((var.get('i')+Js(1.0))))
            if (var.get('rgb').get((var.get('i')+Js(1.0)))>=var.get('max')):
                var.put('max', var.get('rgb').get((var.get('i')+Js(1.0))))
                var.put('maxcolor', (var.get('i')+Js(1.0)))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    if (var.get('maxcolor')==Js(0.0)):
        var.put('h', ((var.get('rgb').get('1')-var.get('rgb').get('2'))/(var.get('max')-var.get('min'))))
    if (var.get('maxcolor')==Js(1.0)):
        var.put('h', (Js(2.0)+((var.get('rgb').get('2')-var.get('rgb').get('0'))/(var.get('max')-var.get('min')))))
    if (var.get('maxcolor')==Js(2.0)):
        var.put('h', (Js(4.0)+((var.get('rgb').get('0')-var.get('rgb').get('1'))/(var.get('max')-var.get('min')))))
    if var.get('isNaN')(var.get('h')):
        var.put('h', Js(0.0))
    var.put('h', (var.get('h')*Js(60.0)))
    if (var.get('h')<Js(0.0)):
        var.put('h', (var.get('h')+Js(360.0)))
    var.put('l', ((var.get('min')+var.get('max'))/Js(2.0)))
    if (var.get('min')==var.get('max')):
        var.put('s', Js(0.0))
    else:
        if (var.get('l')<Js(0.5)):
            var.put('s', ((var.get('max')-var.get('min'))/(var.get('max')+var.get('min'))))
        else:
            var.put('s', ((var.get('max')-var.get('min'))/((Js(2.0)-var.get('max'))-var.get('min'))))
    var.put('s', var.get('s'))
    return Js({'h':var.get('h'),'s':var.get('s'),'l':var.get('l')})
PyJsHoisted_rgbToHsl_.func_name = 'rgbToHsl'
var.put('rgbToHsl', PyJsHoisted_rgbToHsl_)
@Js
def PyJsHoisted_rgbToHwb_(r, g, b, this, arguments, var=var):
    var = Scope({'r':r, 'g':g, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['r', 'bl', 'g', 'h', 'w', 'b'])
    pass
    var.put('r', (var.get('r')/Js(255.0)))
    var.put('g', (var.get('g')/Js(255.0)))
    var.put('b', (var.get('b')/Js(255.0)))
    var.put('max', var.get('Math').callprop('max', var.get('r'), var.get('g'), var.get('b')))
    var.put('min', var.get('Math').callprop('min', var.get('r'), var.get('g'), var.get('b')))
    var.put('chroma', (var.get('max')-var.get('min')))
    if (var.get('chroma')==Js(0.0)):
        var.put('h', Js(0.0))
    else:
        if (var.get('r')==var.get('max')):
            var.put('h', ((((var.get('g')-var.get('b'))/var.get('chroma'))%Js(6.0))*Js(360.0)))
        else:
            if (var.get('g')==var.get('max')):
                var.put('h', (((((var.get('b')-var.get('r'))/var.get('chroma'))+Js(2.0))%Js(6.0))*Js(360.0)))
            else:
                var.put('h', (((((var.get('r')-var.get('g'))/var.get('chroma'))+Js(4.0))%Js(6.0))*Js(360.0)))
    var.put('w', var.get('min'))
    var.put('bl', (Js(1.0)-var.get('max')))
    return Js({'h':var.get('h'),'w':var.get('w'),'b':var.get('bl')})
PyJsHoisted_rgbToHwb_.func_name = 'rgbToHwb'
var.put('rgbToHwb', PyJsHoisted_rgbToHwb_)
@Js
def PyJsHoisted_rgbToCmyk_(r, g, b, this, arguments, var=var):
    var = Scope({'r':r, 'g':g, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['r', 'm', 'g', 'c', 'b', 'y', 'k'])
    pass
    var.put('r', (var.get('r')/Js(255.0)))
    var.put('g', (var.get('g')/Js(255.0)))
    var.put('b', (var.get('b')/Js(255.0)))
    var.put('max', var.get('Math').callprop('max', var.get('r'), var.get('g'), var.get('b')))
    var.put('k', (Js(1.0)-var.get('max')))
    if (var.get('k')==Js(1.0)):
        var.put('c', Js(0.0))
        var.put('m', Js(0.0))
        var.put('y', Js(0.0))
    else:
        var.put('c', (((Js(1.0)-var.get('r'))-var.get('k'))/(Js(1.0)-var.get('k'))))
        var.put('m', (((Js(1.0)-var.get('g'))-var.get('k'))/(Js(1.0)-var.get('k'))))
        var.put('y', (((Js(1.0)-var.get('b'))-var.get('k'))/(Js(1.0)-var.get('k'))))
    return Js({'c':var.get('c'),'m':var.get('m'),'y':var.get('y'),'k':var.get('k')})
PyJsHoisted_rgbToCmyk_.func_name = 'rgbToCmyk'
var.put('rgbToCmyk', PyJsHoisted_rgbToCmyk_)
@Js
def PyJsHoisted_toHex_(n, this, arguments, var=var):
    var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
    var.registers(['n', 'hex'])
    var.put('hex', var.get('n').callprop('toString', Js(16.0)))
    while (var.get('hex').get('length')<Js(2.0)):
        var.put('hex', (Js('0')+var.get('hex')))
    return var.get('hex')
PyJsHoisted_toHex_.func_name = 'toHex'
var.put('toHex', PyJsHoisted_toHex_)
@Js
def PyJsHoisted_cl_(x, this, arguments, var=var):
    var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
    var.registers(['x'])
    var.get('console').callprop('log', var.get('x'))
PyJsHoisted_cl_.func_name = 'cl'
var.put('cl', PyJsHoisted_cl_)
@Js
def PyJsHoisted_w3trim_(x, this, arguments, var=var):
    var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
    var.registers(['x'])
    return var.get('x').callprop('replace', JsRegExp('/^\\s+|\\s+$/g'), Js(''))
PyJsHoisted_w3trim_.func_name = 'w3trim'
var.put('w3trim', PyJsHoisted_w3trim_)
@Js
def PyJsHoisted_isHex_(x, this, arguments, var=var):
    var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
    var.registers(['x'])
    return (Js('0123456789ABCDEFabcdef').callprop('indexOf', var.get('x'))>(-Js(1.0)))
PyJsHoisted_isHex_.func_name = 'isHex'
var.put('isHex', PyJsHoisted_isHex_)
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
example = var.to_python()