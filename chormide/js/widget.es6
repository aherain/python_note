"use strict";


function isPromise(obj) {
    return !!obj && (typeof obj === 'object' || typeof obj === 'function') && typeof obj.then === 'function';
}

function safePromiseEval(__c, __args) {

    __args.__f = function() { return eval(__c) };

    var r = __args.__f();

    if (isPromise(r)) {
        return r;
    }

    return Promise.resolve(r);
}

function* divideByInteger(dividend, divisor) {
    var cur = 0;
    var nxt;
    for (var i = 1; i < divisor; i++) {
        nxt = (i * dividend) / divisor;
        nxt = parseInt(nxt);
        yield [cur, nxt - cur];
        cur = nxt;
    }
    yield [cur, dividend - cur];
    return;
}

function* divideByWeight(dividend, weights) {

    var total_weight = weights.reduce((a, b) => a + b, 0);

    var cur = 0;
    var curfloat = 0;

    weights = weights.slice(0, weights.length - 1);

    for (let w of weights) {
        curfloat += (dividend * w) / total_weight;
        var nxt = parseInt(Math.round(curfloat));
        yield [cur, nxt - cur];
        cur = nxt;
    }
    yield [cur, dividend - cur];

    return;
}

function makePattern(color, p) {
    var pattern = document.createElement('canvas');
    pattern.width = p;
    pattern.height = p;

    var pctx = pattern.getContext('2d');
    pctx.beginPath();
    pctx.strokeStyle = color;
    pctx.moveTo(p, 0);
    pctx.lineTo(0, p);
    pctx.stroke();

    return pattern;
}

window.warnpattern = makePattern('#FF9F9F', 3);
window.highpattern = makePattern('#FFF200', 3);

function draw_symbol(ctx, showtype, ix, iy, stdEm, idata, badge) {

    ctx.save();
    ctx.translate(ix, iy);

    switch (showtype) {

        case 'circle':
            ctx.strokeStyle = (idata == 1) ? "#65A4FC" : "#FF9F9F";
            ctx.fillStyle = (idata == 1) ? "#FFF" : ctx.createPattern(window.warnpattern, "repeat");
            ctx.beginPath();
            ctx.arc(0, 0, Math.abs(stdEm * 0.27), 0, 2 * Math.PI);
            ctx.fill();
            ctx.stroke();
            break;

        case 'drop':
            ctx.strokeStyle = (idata == 1) ? "#a7c600" : "#FF9F9F";
            ctx.fillStyle = (idata == 1) ? "#FFF" : ctx.createPattern(window.warnpattern, "repeat");
            ctx.beginPath();
            ctx.arc(0, stdEm * 0.1, stdEm * 0.20, -Math.PI * 0.25, Math.PI * 1.25);
            ctx.lineTo(0, -stdEm * 0.27);
            ctx.closePath();
            ctx.fill();
            ctx.stroke();
            break;

        case 'door':
            ctx.strokeStyle = (idata == 1) ? "#6f61be" : "#FF9F9F";
            ctx.fillStyle = (idata == 1) ? "#FFF" : ctx.createPattern(window.warnpattern, "repeat");
            ctx.beginPath();
            //ctx.arc(0, 0, stdEm*0.27, 0, 1.5*Math.PI);
            //ctx.arc(stdEm*0.1, -stdEm*0.1, stdEm*0.15, -0.5*Math.PI, 0, true);
            ctx.arc(0, 0, Math.abs(stdEm * 0.27), 0, Math.PI, true);
            ctx.lineTo(-stdEm * 0.27, stdEm * 0.27);
            ctx.lineTo(stdEm * 0.27, stdEm * 0.27);
            ctx.closePath();
            ctx.fill();
            ctx.stroke();
            break;

        case 'triangle':
            if (idata == 1) {
                ctx.strokeStyle = "#4AAC66";
                ctx.fillStyle = "#FFF";
                ctx.beginPath();
                ctx.moveTo(-stdEm * 0.27, stdEm * 0.27);
                ctx.lineTo(stdEm * 0.27, stdEm * 0.27);
                ctx.lineTo(0, -stdEm * 0.27);
                ctx.closePath();
                ctx.fill();
                ctx.stroke();
            } else {
                ctx.strokeStyle = "#FF9F9F";
                ctx.fillStyle = ctx.createPattern(window.warnpattern, "repeat");
                ctx.beginPath();
                ctx.moveTo(-stdEm * 0.27, -stdEm * 0.27);
                ctx.lineTo(stdEm * 0.27, -stdEm * 0.27);
                ctx.lineTo(0, stdEm * 0.27);
                ctx.closePath();
                ctx.fill();
                ctx.stroke();
            }
            break;

        case 'square':
            ctx.strokeStyle = (idata == 1) ? "#40BEE5" : "#FF9F9F";
            ctx.fillStyle = (idata == 1) ? "#FFF" : ctx.createPattern(window.warnpattern, "repeat");
            ctx.beginPath();
            ctx.rect(-stdEm * 0.27, -stdEm * 0.27, stdEm * 0.54, stdEm * 0.54);
            ctx.fill();
            ctx.stroke();
            break;

        case 'pentagon':
            ctx.strokeStyle = (idata == 1) ? "#9240e5" : "#FF9F9F";
            ctx.fillStyle = (idata == 1) ? "#FFF" : ctx.createPattern(window.warnpattern, "repeat");
            ctx.beginPath();
            ctx.moveTo(-stdEm * 0.28 * 0.62, stdEm * 0.28);
            ctx.lineTo(stdEm * 0.28 * 0.62, stdEm * 0.28);
            ctx.lineTo(stdEm * 0.28, -stdEm * 0.28 * 0.2);
            ctx.lineTo(0, -stdEm * 0.29);
            ctx.lineTo(-stdEm * 0.28, -stdEm * 0.28 * 0.2);
            ctx.closePath();
            ctx.fill();
            ctx.stroke();
            break;

        case 'hexagonal':
            ctx.strokeStyle = (idata == 1) ? "#e67e47" : "#FF9F9F";
            ctx.fillStyle = (idata == 1) ? "#FFF" : ctx.createPattern(window.warnpattern, "repeat");
            ctx.beginPath();
            ctx.moveTo(-stdEm * 0.27, stdEm * 0.3 * 0.5);
            ctx.lineTo(0, stdEm * 0.3);
            ctx.lineTo(stdEm * 0.27, stdEm * 0.3 * 0.5);
            ctx.lineTo(stdEm * 0.27, -stdEm * 0.3 * 0.5);
            ctx.lineTo(0, -stdEm * 0.3);
            ctx.lineTo(-stdEm * 0.27, -stdEm * 0.3 * 0.5);
            ctx.closePath();
            ctx.fill();
            ctx.stroke();
            break;

    }

    if (badge) {
        switch (badge) {

            case 0:
                break;

            case 1:
                ctx.strokeStyle = "#444";
                ctx.beginPath();
                ctx.moveTo(-stdEm * 0.4, -stdEm * 0.13);
                ctx.lineTo(stdEm * 0.4, stdEm * 0.13);
                ctx.stroke();
                break;

            case 2:
                ctx.translate(stdEm * 0.25, stdEm * 0.25);
                ctx.strokeStyle = "#FF9F9F";
                ctx.fillStyle = ""
                ctx.beginPath();
                ctx.arc(0, 0, Math.abs(stdEm * 0.27) * 0.1, 0, 2 * Math.PI);
                ctx.fill();
                ctx.stroke();
                break;

        }

    }

    ctx.restore();

}

class Sprite {

    constructor(parent, x, y, w, h, dragable = false) {

        this._map = new WeakMap();
        this._map.parent = parent;

        this.x = x;
        this.y = y;
        this.w = w;
        this.h = h;
        this.x2 = x + w;
        this.y2 = y + h;

        this.dragable = dragable;

        this._ondragend = (evt) => this.dragEnd(evt.clientX, evt.clientY);
        this._ondragmove = (evt) => this.dragMove(evt.clientX, evt.clientY);
    }

    setPosSize(x, y, w, h) {
        this.x = x;
        this.y = y;
        this.w = w;
        this.h = h;
        this.x2 = x + w;
        this.y2 = y + h;
    }

    get parent() {
        return this._map.parent;
    }

    hitTest(x, y) {
        return (x >= this.x && x <= (this.x + this.w) && y >= this.y && y <= (this.y + this.h));
    }

    dragStart(x, y) {

        this.sx = this.x;
        this.sy = this.y;

        this.sw = this.w;
        this.sh = this.h;

        this.sx2 = this.x2;
        this.sy2 = this.y2;

        this.mousex = x;
        this.mousey = y;

        document.addEventListener('mouseup', this._ondragend);
        document.addEventListener('mousemove', this._ondragmove);

    }

    dragEnd(x, y) {

        document.removeEventListener('mouseup', this._ondragend);
        document.removeEventListener('mousemove', this._ondragmove);
    }

    dragMove(x, y) {

        [x, y] = this.parent.mouseToCanvasPostion(x, y);

        this.x = this.sx + x - this.mousex;
        this.y = this.sy + y - this.mousey;

        this.parent.redraw();
    }
}

class ScrollBar extends Sprite {

    constructor(parent, bx, by, bw, bh, s) {

        var h = bh * s;
        super(parent, bx, by, bw, h, true);

        this.bx = bx;
        this.by = by;
        this.bw = bw;
        this.bh = bh;

        this.p = 0;

    }

    dragMove(x, y) {

        [x, y] = this.parent.mouseToCanvasPostion(x, y);

        this.y = this.sy + y - this.mousey;
        this.y = Math.max(this.by, this.y);
        this.y = Math.min(this.by + this.bh - this.h, this.y);

        this.p = (this.y - this.by) / (this.bh - this.h);

        this.parent.redraw();

    }

    setP(p) {
        p = Math.max(0, p);
        p = Math.min(1, p);
        this.p = p;
        this.y = this.p * (this.bh - this.h) + this.by;

        this.parent.redraw();

    }
}


class ScrollBarH extends Sprite {

    constructor(parent, bx, by, bw, bh, w) {

        super(parent, bx, by, w, bh, true);

        this.bx = bx;
        this.by = by;
        this.bw = bw;
        this.bh = bh;

        this.p = 0;

    }

    dragEnd(x, y) {
        super.dragEnd(x, y);
        this.parent.sprite_dragEnd(this, x, y);
        this.parent.redraw();
    }

    dragMove(x, y) {

        [x, y] = this.parent.mouseToCanvasPostion(x, y);

        this.x = this.sx + x - this.mousex;
        this.x = Math.max(this.bx, this.x);
        this.x = Math.min(this.bx + this.bw - this.w, this.x);

        this.p = (this.x - this.bx) / (this.bx - this.x);

        this.parent.redraw(1);

    }

}


class DataGrid extends HTMLElement {

    constructor() {
        super();
        this.flexible = true;
        this.clickable = true;
        this.spritedragable = true;
        this.watchcursor = false;
        this._domloaded = false;
        this.cw = 0;
        this.rh = 0;
        this.x = 0;
        this.y = 0;
        this.cm = 0; // 列总数
        this.rm = 0; // 行总数
        this.ci = 0; // 当前列index
        this.ri = 0; // 当前行index
        this.leftw = 1; // grid左边列宽
        this.rightw = 1; // grid右边列宽
    }

    connectedCallback() {

        var ks = [];
        var ps = [];

        this.innerHTML = `
    <style scoped>
  .ant-spin-dot {
    width: 32px;
    height: 32px;
    position: absolute;
    left:0;
    right:0;
    top:0;
    bottom:0;
    margin: auto;
    display: inline-block;
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
    -webkit-animation: antRotate 1.2s infinite linear;
    animation: antRotate 1.2s infinite linear;
  }
  .ant-spin-dot i{
    width: 9px;
    height: 9px;
    border-radius: 100%;
    background-color: #108ee9;
    -webkit-transform: scale(.75);
    transform: scale(.75);
    display: block;
    position: absolute;
    opacity: .3;
    -webkit-animation: antSpinMove 1s infinite linear alternate;
    animation: antSpinMove 1s infinite linear alternate;
    -webkit-transform-origin: 50% 50%;
    transform-origin: 50% 50%;
  }
  .ant-spin-dot i:first-child {
    left: 0;
    top: 0;
  }
  .ant-spin-dot i:nth-child(2) {
    right: 0;
    top: 0;
    -webkit-animation-delay: .4s;
    }
    .ant-spin-dot i:nth-child(3) {
        right: 0;
        bottom: 0;
        -webkit-animation-delay: .8s;
        animation-delay: .8s;
    }
    .ant-spin-dot i:nth-child(4) {
        left: 0;
        bottom: 0;
        -webkit-animation-delay: 1.2s;
        animation-delay: 1.2s;
    }

  @-webkit-keyframes antRotate {
      0% {
        transform: rotate(0deg);
      }
      50% {
        transform: rotate(180deg);
      }
      100% {
           transform: rotate(360deg);
      }
  }

  @keyframes antRotate {
    0% {
        transform: rotate(0deg);
      }
      50% {
        transform: rotate(180deg);
      }
      100% {
           transform: rotate(360deg);
      }
  }

  @-webkit-keyframes antSpinMove {
    to{opacity:1}
  }

  @keyframes antSpinMove {
    to{opacity:1}
  }
  </style>

  <span class="ant-spin-dot"><i></i><i></i><i></i><i></i></span>
  `;
        //   <div class="load-container load6">
        //        <div class="loader">Loading...</div>
        //   </div>

        if (this.prepare) {
            for (let [k, ep] of this.prepare) {
                let r = eval(this.getAttribute(ep));
                let p = isPromise(r) ? r : Promise.resolve(r);
                ks.push(k);
                ps.push(p);
            }
        }

        if (ps) {
            Promise.all(ps).then(rs => this._prepare2(ks, rs))
        } else {
            this._init([], []);
        }
    }

    prepare_args(x) {}

    _prepare2(ks1, rs1) {

        var m = {};
        for (let i = 0; i < ks1.length; i++) {
            m[ks1[i]] = rs1[i];
        }

        this.prepare_args(m);

        var ks = [];
        var ps = [];

        if (this.prepare2) {

            for (let [k, ep] of this.prepare2) {
                ks.push(k);
                ps.push(safePromiseEval(this.getAttribute(ep), m));
            }

            Promise.all(ps).then(rs => this._init([...ks, ...ks1], [...rs, ...rs1]))

        } else {
            this._init(ks1, rs1);
        }

    }

    _init(ks, rs) {


        var m = {};
        for (let i = 0; i < ks.length; i++) {
            m[ks[i]] = rs[i];
        }

        this.sprites = [];

        this.innerHTML = '';

        this.init(m);

        if (!this.innerHTML) {
            this.innerHTML = '<canvas></canvas>'
        }

        this.layers = this.querySelectorAll(':scope > canvas');
        this.layers = Array.apply(null, this.layers).reverse();
        //this.can = this.querySelector('canvas');
        this.can = this.layers[0];
        this.cnt = this.can.parentElement;

        if (this.flexible) {
            window.addEventListener('resize', (evt) => this.onResize());
        }
        if (this.clickable) {
            this.can.addEventListener('mousedown', (evt) => this.onMouseDown(evt.clientX, evt.clientY, event.button));
            this.can.addEventListener('click', (evt) => this.onClick(evt.clientX, evt.clientY, true, false));
            this.can.addEventListener('contextmenu', (evt) => {
                evt.preventDefault();
                this.onClick(evt.clientX, evt.clientY, false, false);
            });
            this.can.addEventListener('dblclick', (evt) => this.onClick(evt.clientX, evt.clientY, true, true));
            this.can.addEventListener('mousewheel', (evt) => this.onWheel(evt.clientX, evt.clientY, evt.wheelDelta ? evt.wheelDelta : -evt.detail));
            document.addEventListener('keyup', (evt) => this.onKeyup(evt, false));
        }
        if (this.watchcursor) {
            document.addEventListener('mousemove', (evt) => this._onCursorMove(evt.clientX, evt.clientY));
        }
        if (document.readyState != 'complete') {
            this._onwindowload = (evt) => this.onWindowLoad();
            window.addEventListener('load', this._onwindowload);
        } else {
            this._domloaded = true;
            this.onResize();
        }

        this._dragOrClick = 'click';
        this._dragSprite = null;

    }

    onWindowLoad() {
        this._domloaded = true;
        this.onResize();
        window.removeEventListener('load', this._onwindowload);
    }

    init(args) {}

    disconnectedCallback() {}

    onResize() {

        if (this._domloaded == false) return;

        this.canvasWidth = this.cnt.clientWidth;
        this.canvasHeight = this.cnt.clientHeight;

        for (let layer of this.layers) {
            layer.width = this.cnt.clientWidth;
            layer.height = this.cnt.clientHeight;
            layer.style.position = 'absolute';
            layer.style.zIndex = '0';
        }

        this.layout();
        this.redraw();

    }

    hitTestSprites(x, y) {

        for (let i = this.sprites.length - 1; i >= 0; i -= 1) {
            var s = this.sprites[i];
            if (s.hitTest(x, y)) {
                return s;
            }
        }

        return;

    }

    popHitSprites(x, y) {

        for (let i = this.sprites.length - 1; i >= 0; i -= 1) {
            var s = this.sprites[i];
            if (s.hitTest(x, y)) {
                this.sprites.splice(i, 1);
                return s;
            }
        }

        return;
    }

    mouseToCanvasPostion(x, y) {

        x = x - this.can.offsetLeft;
        y = y - this.can.offsetTop;

        var pe = this.can.offsetParent;
        console.log('>>>点击效果')
            /*
                    原：x = x - pe.offsetLeft;
                    问题：滚动后定位错误
                    解决：x 加 scrollLeft
            */
        while (pe != null) {
            x = x - pe.offsetLeft + pe.scrollLeft;
            y = y - pe.offsetTop;

            pe = pe.offsetParent;
        }

        return [x, y];
    }

    onMouseDown(x, y, mbtn) {

        if (mbtn != 0) { return; }

        [x, y] = this.mouseToCanvasPostion(x, y);

        var s = null;
        if (this.spritedragable) {
            s = this.hitTestSprites(x, y);
        }

        if (s) {
            this._dragSprite = s;
            s.dragStart(x, y);
            this._dragOrClick = 'drag';
        } else {
            this._dragOrClick = 'click';
        }
    }

    onClick(x, y, left, doubleclick) {

        if (this._dragOrClick == 'drag') {
            this._dragSprite = null;
            this._dragOrClick = 'click';
            return;
        }

        [x, y] = this.mouseToCanvasPostion(x, y);

        var ct, cv, ci, cm, cx, cw;
        var rt, rv, ri, rm, ry, rh;
        var cindex = 0;
        for ([ct, cv, ci, cm, cx, cw] of this.cols) {
            if (x >= cx && x < cx + cw) {
                if (cindex === 0) {
                    this.leftw = cw;
                    this.rightw = this.cols[1][5];
                } else if (cindex === (this.cols.length - 1)) {
                    this.leftw = this.cols[cindex - 1][5];
                    this.rightw = cw;
                } else {
                    this.leftw = this.cols[cindex - 1][5];
                    this.rightw = this.cols[cindex + 1][5];
                }
                break;
            }
            cindex++;
        }

        for ([rt, rv, ri, rm, ry, rh] of this.rows) {
            if (y >= ry && y < ry + rh) {
                break;
            }
        }
        this.cw = cw;
        this.rh = rh;
        this.x = x;
        this.y = y;
        this.cm = cm;
        this.rm = rm;
        this.ci = ci;
        this.ri = ri;
        var zone = rt + ct;
        var prefix = (left) ? ('on') : ('onR');
        prefix += doubleclick ? ('DblClick_') : ('Click_');
        var cb = this[prefix + zone];
        if (cb) {
            this[prefix + zone](ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y);
        } else if (rt === 't') {
            this.copyTableFoot(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y);
        }
    }
    onKeyup(evt, switch_flag) {
        if (evt.keyCode > 36 && evt.keyCode < 41 && this.cw && this.rh) {
            var tempx = this.x;
            var tempy = this.y;
            var tempci = this.ci;
            var tempri = this.ri;
            switch (evt.keyCode) {
                case 37: // left
                    tempci--;
                    tempx -= this.leftw;
                    break;
                case 38: // up
                    tempri--;
                    tempy -= this.rh;
                    break;
                case 39: // right
                    tempci++;
                    tempx += this.rightw;
                    break;
                case 40: // down
                    tempri++;
                    tempy += this.rh;
                    break;
            }
            var ct, cv, ci, cm, cx, cw;
            var rt, rv, ri, rm, ry, rh;
            if (tempci < 0 || tempri < 0 || tempci >= this.cm || tempri >= this.rm) {
                return;
            } else {
                this.x = tempx;
                this.y = tempy;
                // this.ci = tempci;
                // this.ri = tempri;
            }
            var cindex = 0;
            for ([ct, cv, ci, cm, cx, cw] of this.cols) {
                if (this.x >= cx && this.x < cx + cw) {
                    if (cindex === 0) {
                        this.leftw = cw;
                        this.rightw = this.cols[1][5];
                    } else if (cindex === (this.cols.length - 1)) {
                        this.leftw = this.cols[cindex - 1][5];
                        this.rightw = cw;
                    } else {
                        this.leftw = this.cols[cindex - 1][5];
                        this.rightw = this.cols[cindex + 1][5];
                    }
                    break;
                }
                cindex++;
            }
            for ([rt, rv, ri, rm, ry, rh] of this.rows) {
                if (this.y >= ry && this.y < ry + rh) {
                    break;
                }
            }
            this.ci = ci;
            this.ri = ri;
            var zone = rt + ct
            var prefix = 'onClick_';
            var cb = this[prefix + zone];
            if (cb) {
                this[prefix + zone](ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, this.x, this.y);
            }
            event.preventDefault();
        }
    }

    onWheel(x, y, delta) {

        [x, y] = this.mouseToCanvasPostion(x, y);
        delta = (delta > 0) ? 1 : -1;

        var ct, cv, ci, cm, cx, cw;
        var rt, rv, ri, rm, ry, rh;
        for ([ct, cv, ci, cm, cx, cw] of this.cols) {
            if (x >= cx && x < cx + cw) {
                break;
            }
        }

        for ([rt, rv, ri, rm, ry, rh] of this.rows) {
            if (y >= ry && y < ry + rh) {
                break;
            }
        }

        var zone = rt + ct;
        var prefix = 'onWheel_';
        var cb = this[prefix + zone];

        if (cb) {
            this[prefix + zone](ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y, delta);
        }

    }

    _onCursorMove(x, y) {
        //var x, y;
        //[x, y] = this.mouseToCanvasPostion(evt.clientX, evt.clientY);
        [x, y] = this.mouseToCanvasPostion(x, y);
        this.onCursorMove(x, y);
    }

    onCursorMove(x, y) {}

    draw(deep) {}

    layout() {}

    redraw(deep = null) {

        if (this._domloaded == false) return;

        if (deep == null) {
            deep = this.layers.length - 1;
        }
        //this.can.width = this.cnt.clientWidth;
        for (let d = Math.min(deep, this.layers.length - 1); d >= 0; d--) {
            this.layers[d].width = this.cnt.clientWidth;
        }
        this.draw(deep);

    }
}


class RollDataGrid extends DataGrid {

    constructor() {
        super();
        this.prepare = [
            ['fulldata', 'fetchdata'],
            ['coldata', 'coldata'],
            ['rowheight', 'rowheight'],
            ['isnotfoot', 'isnotfoot']
        ];

    }

    getSelectRows() {
        var showdata = [];

        if (this.subtotalselect) {
            for (let i = 0; i < this.stdata.length; i++) {
                if (this.subtotaltype === 1) {
                    showdata.push(this.stdata[i]);
                    for (let d of this.istdata[i]) {
                        showdata.push(d);
                    }
                } else if (this.subtotaltype === 2) {
                    for (let d of this.istdata[i]) {
                        showdata.push(d);
                    }
                    showdata.push(this.stdata[i]);
                } else {
                    showdata.push(this.stdata[i]);
                }

            }
        } else {
            showdata = this.data;
        }
        var sdata = [];
        this.rowselect.forEach(r => {
            // sdata.push(this.fulldata[r]);
            sdata.push({});
        });

        var dy = this.y - this.ry;

        var ln = 0;


        var by = parseInt(this.sprites[0].p * ((showdata.length + 1) * this.row_h - this.rh));

        for (let dk of showdata) {
            if (typeof dk === 'number') {
                var d = this.fulldata[dk];

                var ly8 = (ln + 0) * this.row_h - by;
                var ly2 = (ln + 1) * this.row_h - by;

                if (dy >= ly8 && dy <= ly2) {
                    sdata[0] = d;
                    break;
                }
            }
            ln += 1;
        }
        // console.log(sdata);
        return sdata;
    }

    init(args) {

        this.innerHTML = `
    <style scoped>
    .rdg_dropdown {
  border: 1px solid #eee; 
  position: absolute;
  background-color: #fff;
  box-shadow: 2px 2px 3px #888888;
  display: none;
  font-family: 微软雅黑;
    }
    .rdg_fopt {
  font-size: 14px;
  padding: 3px 0px 3px 33px;

    }
    .rdg_fopt:hover {
  background-color: #f0f0f0;
    }

    .rdg_fopt img {
  display: block;
  float: left;
  margin-left: -28px;
  vertical-align:middle;
    }
    .rdg_fopt a {
    color: #555555;
    }

    .rdg_sorter span{
  vertical-align:middle;
    }

    .rdg_subtotal span{
  vertical-align:middle;
    }

    .rdg_filter {
      padding: 5px;
      padding-left: 33px;
    }

    .rdg_selectbox {
      border: 1px solid #E2E4E7;
      min-height: 100px;
      max-height: 300px;
      overflow-y: auto;
      font-size: 12px;
      padding: 5px;
    }

    .rdg_selectbtn {
  padding: 6px;
  float: right;
    }

    .rds_dropdown {
      border: 1px solid #eee; 
      position: absolute;
      background-color: #fff;
      box-shadow: 2px 2px 3px #888888;
      display: none;
      font-family: 微软雅黑;
    }

    .rds_selectbox {
      border: 1px solid #E2E4E7;
      min-height: 100px;
      max-height: 300px;
      overflow-y: auto;
      font-size: 12px;
      padding: 5px;
    }

    .rds_title {
      padding: 8px;
    }

    .rds_filter {
      padding: 5px;
    }

    .rds_select_col {
      width: 120px;
    }

    .rds_select_sort {
      width: 50px;
    }

    .rds_selectbtn {
      padding: 6px;
      float: right;
    }

    input[type=text] {
    }
    </style>
    <canvas></canvas>
    <div class="rdg_dropdown">
     <div class="rdg_fopt rdg_sorter" onclick="this.offsetParent.parentElement.onSort(true);"><img src="assets/img/sortAZ.png" /><span>升序排列</span></div>
     <div class="rdg_fopt rdg_sorter" onclick="this.offsetParent.parentElement.onSort(false);"><img src="assets/img/sortZA.png" /><span>降序排列</span></div>
     <div class="rdg_fopt rdg_sorter rdg_absolute_up" onclick="this.offsetParent.parentElement.onAbsoluteSort(true);"><img src="assets/img/sortZA.png" /><span>绝对值升序</span></div>
     <div class="rdg_fopt rdg_sorter rdg_absolute_down" onclick="this.offsetParent.parentElement.onAbsoluteSort(false);"><img src="assets/img/sortZA.png" /><span>绝对值降序</span></div>
     <div class="rdg_fopt rdg_subtotal">
        <a onclick="this.offsetParent.parentElement.onSubtotals(0);">分类汇总</a>
        <a onclick="this.offsetParent.parentElement.onSubtotals(1);"><img style="float:right" src="assets/img/subtotals_up.png" /></a>
        <a onclick="this.offsetParent.parentElement.onSubtotals(2);"><img style="float:right;margin-right:20px;" src="assets/img/subtotals_down.png" /></a>
     </div>
     <div class="rdg_fopt rdg_unsubtotal" onclick="this.offsetParent.parentElement.onSubtotals(3);"><span>取消分类汇总</span></div>
     <div class="rdg_filter">
      <div style="padding: 4px; padding-left:0px">
        <input type="text" style="width:100%;" onchange="RollDataGrid.selectfilt(this);" />
      </div>
      <div class="rdg_selectbox">
      </div>
      <div class="rdg_selectbtn">
       <button onclick="this.parentElement.previousElementSibling.querySelectorAll('input').forEach(c=>c.checked=true);">全选</button>
       <button onclick="this.parentElement.previousElementSibling.querySelectorAll('input').forEach(c=>c.checked=false);">清除</button>
       <button onclick="this.offsetParent.parentElement.onFilter();">应用</button>
       <button onclick="this.offsetParent.style['display']='none';">取消</button>
      </div>
     </div>
    </div>
    <div class="rds_dropdown">
     <div class="rds_title">自定义排序</div>
     <div class="rds_filter">
      <div class="rds_selectbox">
      </div>
      <div class="rds_selectbtn">
       <button onclick="this.offsetParent.parentElement.onSorter();">应用</button>
       <button onclick="this.offsetParent.style['display']='none';">取消</button>
      </div>
     </div>
    </div>
    `;

        this.dropdown = this.querySelector('div.rdg_dropdown');
        this.dropdownSort = this.querySelector('div.rds_dropdown');
        this.selectSortCols = []; // 存储自定义排序

        this.fulldata = args['fulldata']; //eval(this.getAttribute('fetchdata')); // 取消筛选时用
        // this.fulldataBAK = [];
        // for (let fd of this.fulldata) {
        // 	const obj = {};
        // 	for (let o of Object.keys(fd)) {
        // 		obj[o] = fd[o];
        // 	}
        // 	this.fulldataBAK.push(obj);
        // }
        // this.fulldataBAK = Object.assign({}, args['fulldata']); int转成了str
        // console.log(this.fulldata);
        // console.log(this.fulldataBAK);
        this.coldata = args['coldata']; //eval(this.getAttribute('coldata'));
        this.isnotfoot = args['isnotfoot']; // true是没有foot，不传或者false是有完整foot
        this.colmap = new Map(this.coldata.map((i) => [i['key'], i]));
        this.filterdata = new Map();
        this.sortselect = null;
        this.subtotalselect = null;
        this.rowselect = new Set();
        this.data = Array.from(new Array(this.fulldata.length), (val, index) => index);
        this._summaryOK = false;
        this.z_rA_font = '14px 微软雅黑';
        this.z_stA_font = '12px 微软雅黑';
        this.z_stA_st_font = '10px 微软雅黑';
        this.z_rB_font = '14px 微软雅黑';
        this.z_stB_font = '12px 微软雅黑';
        this.z_stB_micro_font = '11px 微软雅黑'
        this.z_stB_mini_font = '10px 微软雅黑'
        this.z_stB_st_font = 'bold 12px 宋体';

        this.buttons = [];

        this.row_h = 25;
        if (args['rowheight']) {
            this.row_h = parseInt(args['rowheight']);
        }

        this.onrunselect = this.getAttribute('onrunselect');
        this.OnClick = this.getAttribute('OnClick');


        //this.money_re = new RegExp('(\d{1,3})(?=(\d{3})+(?:$|\.))','g');
        this.money_re = /(\d)(?=(\d{3})+\.)/g;

        this.onexport = false;
    }

    static selectfilt(inp) {
        let opts = inp.parentElement.nextElementSibling.children;
        let divs = inp.parentElement.nextElementSibling;
        divs['hidden'] = true;
        for (let opt of opts) {
            if (opt.querySelector('span').innerText.includes(inp.value)) {
                opt.hidden = '';
            } else {
                opt.hidden = 'hidden';
            }
        }
        divs['hidden'] = false;
    }

    layout() {

        if (this._summaryOK == false) {
            this.summary();
            this._summaryOK = true;
        }

        this.z_r_h = 60;
        if (this.isnotfoot) {
            this.z_t_h = 30;
        } else {
            this.z_t_h = 90;
        }
        this.z_s_h = this.canvasHeight - this.z_r_h - this.z_t_h;

        this.z_C_w = 50;
        this.z_B_w = this.canvasWidth - this.z_A_w - this.z_C_w;

        this.z_AB_w = this.z_A_w + this.z_B_w;

        this.cols = [];
        this.rows = [];

        this.cols.push(['A', '行号', 0, 1, 0, this.z_A_w]);

        var x = this.z_A_w;
        var idx = 0;
        for (let c of this.coldata) {
            var w = parseInt(this.z_B_w * c['width'] / this.col_totalw);
            this.cols.push(['B', c, idx, this.coldata.length, x, w]);
            x += w;
            idx += 1;
        }

        this.cols.push(['C', null, 0, 1, this.z_A_w + this.z_B_w, this.z_C_w]);

        this.sprites = [];
        this.sprites.push(new ScrollBar(this, this.canvasWidth - 20, this.z_r_h + 20, 20, this.z_s_h - 40 - 50, 0.1));

        var y = 0
        this.rows.push(['r', '', 0, 1, y, this.z_r_h]);
        y += this.z_r_h;
        this.rows.push(['s', '', 0, 1, y, this.z_s_h]);
        y += this.z_s_h;
        this.rows.push(['t', '', 0, 1, y, this.z_t_h]);

    }

    summary() {

        var ctx = this.can.getContext('2d');

        this.totaldata = {};
        this.optiondata = {};
        this.col_totalw = 0;
        this.watchcols = [];

        for (let col of this.coldata) {

            ctx.font = this.z_stB_font;

            var k = col['key'];
            var w = col['w'];
            var t = null;
            var opts = [];

            if (col['watch']) {
                this.watchcols.push(col);
            }

            switch (col.type) {

                case 'str':
                    if (col.dispose) {
                        w = this.fulldata.reduce((a, b) => Math.max(a, ctx.measureText(b[k]).width), 0);
                        opts = Array.from(new Set(this.fulldata.map(a => a[k] ? a[k].substr(0, 7) : null))).sort();
                        t = opts.length;
                    } else {
                        w = this.fulldata.reduce((a, b) => Math.max(a, ctx.measureText(b[k]).width), 0);

                        opts = Array.from(new Set(this.fulldata.map(a => a[k]))).sort();
                        t = opts.length;
                    }
                    if (w < 25) { w = 25; } else if (w > 166) { w = 166; }
                    break;

                case 'int':

                    this.fulldata.forEach(function(a) { a[k] = parseInt(a[k]) });

                    var pds = this.fulldata.reduce((a, b) => a + Math.max(b[k], 0), 0);
                    var nds = this.fulldata.reduce((a, b) => a + Math.min(b[k], 0), 0);
                    w = Math.max(ctx.measureText('' + pds).width, ctx.measureText('' + nds).width);

                    t = this.fulldata.reduce((a, b) => a + b[k], 0);

                    opts = ['负数', '0', '正数'];

                    break;

                case 'money':

                    this.fulldata.forEach(function(a) { a[k] = parseInt(a[k]) });

                    var pds = this.fulldata.reduce((a, b) => a + Math.max(b[k], 0), 0);
                    var nds = this.fulldata.reduce((a, b) => a + Math.min(b[k], 0), 0);
                    pds = (pds / 100).toFixed(2).replace(this.money_re, "$1,");
                    nds = (nds / 100).toFixed(2).replace(this.money_re, "$1,");
                    w = Math.max(ctx.measureText(pds).width, ctx.measureText(nds).width);

                    t = this.fulldata.reduce((a, b) => a + b[k], 0);

                    opts = ['负数', '0', '正数'];

                    break;

                case 'button':

                    w = this.fulldata.reduce((a, b) => Math.max(a, ctx.measureText(b[k] || '').width), 0);
                    w = w + 10;

                    opts = Array.from(new Set(this.fulldata.map(a => a[k] || '[N/A]'))).sort();
                    t = opts.length;

                    break;
            }

            ctx.font = this.z_rB_font;
            w = col['display'].split('\n').reduce((a, b) => Math.max(a, ctx.measureText(b).width), w);

            col['width'] = parseInt(w) + 20;
            this.totaldata[k] = t;
            this.optiondata[k] = opts;

            this.col_totalw += col['width'];

        }

        ctx.font = this.z_stA_font;
        this.z_A_w = parseInt(ctx.measureText(this.fulldata.length).width) + 30;

        ctx.font = this.z_rA_font;
        this.z_A_w = Math.max((parseInt(ctx.measureText('行号').width) + 30), this.z_A_w)

        this.sumdata = this.totaldata;

        this.calcProportionData();

    }

    calcProportionData() {

        this.propdata = {};

        for (let col of this.coldata) {

            var k = col['key'];
            var t = null;

            switch (col.type) {

                case 'int':
                case 'money':
                    t = (this.sumdata[k] * 100 / this.totaldata[k]);
                    if (t == NaN) {
                        t = 'N/A';
                    } else if (t > 10000 || t < -10000) {
                        t = '###';
                    } else if (t >= 100 || t <= -100) {
                        t = Math.round(t).toFixed(0);
                        t = '' + t + '%';
                    } else {
                        t = (Math.round(t * 100) / 100).toFixed(2);
                        t = '' + t + '%';
                    }
                    break;

                default:
                    t = ''
                    break;

            }

            this.propdata[k] = t;
        }

    }

    calcSumData() {

        this.sumdata = {};

        for (let col of this.coldata) {

            var k = col['key'];
            var t = null;

            switch (col.type) {

                case 'int':
                case 'money':
                    t = this.data.reduce((a, b) => a + this.fulldata[b][k], 0);
                    break;

                default:
                    t = (new Set(this.data.map(a => this.fulldata[a][k]))).size;
                    break;

            }

            this.sumdata[k] = t;
        }

    }

    calcSelectData() {

        this.sumselectdata = {};

        var showdata = [];

        if (this.subtotalselect) {
            for (let i = 0; i < this.stdata.length; i++) {
                if (this.subtotaltype === 1) {
                    showdata.push(this.stdata[i]);
                    for (let d of this.istdata[i]) {
                        showdata.push(d);
                    }
                } else if (this.subtotaltype === 2) {
                    for (let d of this.istdata[i]) {
                        showdata.push(d);
                    }
                    showdata.push(this.stdata[i]);
                } else {
                    showdata.push(this.stdata[i]);
                }
            }
        } else {
            showdata = this.data;
        }
        for (let col of this.coldata) {

            var k = col['key'];
            var t = null;

            switch (col.type) {

                case 'button':
                    t = null;
                    break;

                case 'int':
                case 'money':
                    if (this.subtotalselect) {
                        // if (this.subtotaltype === 0) {
                        //     t = Array.from(this.rowselect).reduce((a, b) => a + (typeof showdata[b] === 'number') ? this.fulldata[showdata[b]][k] : showdata[b][k], 0);
                        // } else {

                        // }
                        // t = Array.from(this.rowselect).reduce((a, b) => a + (typeof showdata[b] === 'number') ? this.fulldata[showdata[b]][k] : showdata[b][k], 0);
                        let sub = 0;
                        for (let r of this.rowselect) {
                            if (this.subtotaltype === 0) {
                                sub += showdata[r][k];
                            } else {
                                sub += this.fulldata[showdata[r]][k];
                            }
                        }
                        t = sub;
                    } else {
                        // t = Array.from(this.rowselect).reduce((a, b) => a + this.fulldata[this.data[b]][k], 0);
                        let sub = 0;
                        for (let r of this.rowselect) {
                            sub += this.fulldata[this.data[r]][k];
                        }
                        t = sub;
                    }
                    break;

                default:
                    if (this.subtotalselect) {
                        // t = Array.from(this.rowselect).reduce((a, b) => (new Set([...a, ...this.fulldata[showdata[b]][k]])), (new Set()));
                        t = new Set(this.rowselect);
                    } else {
                        t = (new Set(Array.from(this.rowselect).map(a => this.fulldata[this.data[a]][k])));
                    }
                    t = t.size;
                    break;

            }

            this.sumselectdata[k] = t;
        }

    }

    draw(deep) {

        var ctx = this.can.getContext('2d');

        this.draw_thead(ctx, 0, 0, this.z_AB_w, this.z_r_h);
        this.draw_tbody(ctx, 0, this.z_r_h, this.z_AB_w, this.z_s_h);
        this.draw_scroll(ctx, this.z_AB_w, this.z_r_h, this.z_C_w, this.z_s_h);
        this.draw_tfoot(ctx, 0, this.z_r_h + this.z_s_h, this.z_AB_w, this.z_t_h);

        ctx.fillStyle = '#CECECE';
        ctx.fillRect(this.sprites[0].x + 1, this.sprites[0].y, this.sprites[0].w - 2, this.sprites[0].h);


        ctx.save();
        ctx.translate(this.canvasWidth - 3, this.canvasHeight - 3);

        ctx.fillStyle = '#666';
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(-13, 0);
        ctx.lineTo(0, -13);
        ctx.closePath()
        ctx.fill();

        ctx.fillStyle = '#aaa';
        ctx.font = '11px 微软雅黑';
        ctx.textAlign = 'right';
        ctx.textBaseline = 'bottom';
        ctx.fillText(this.onexport ? '保存中' : '导出', -14, 2);

        ctx.restore();

    }

    draw_thead(ctx, x, y, w, h) {

        ctx.save();
        ctx.translate(x, y);

        ctx.fillStyle = "#FAFAFA";
        ctx.fillRect(0, 0, this.canvasWidth, h);

        ctx.beginPath();
        ctx.strokeStyle = "#F0F0F0";
        ctx.moveTo(0, h - 0.5);
        ctx.lineTo(this.canvasWidth, h - 0.5);
        ctx.stroke();

        ctx.textBaseline = 'middle';
        ctx.fillStyle = "#444";

        for (let [ct, cv, ci, cm, cx, cw] of this.cols) {

            ctx.beginPath();
            ctx.strokeStyle = "#F0F0F0";
            ctx.moveTo(cx + cw - 0.5, 0);
            ctx.lineTo(cx + cw - 0.5, h);
            ctx.stroke();

            var tx;
            var ty;

            switch (ct) {

                case 'A':
                    ctx.font = this.z_rA_font;

                    ctx.textAlign = 'right';
                    tx = cx + cw - 15;
                    ty = h - 5 - 9;
                    ctx.fillText(cv, tx, ty);

                    ctx.font = '16px FontAwesome';
                    ctx.fillStyle = '#bbb'

                    ctx.fillText('\uf0dc', cx + 20, 10);

                    break;

                case 'B':

                    ctx.font = this.z_rB_font;

                    ctx.textAlign = cv['align']

                    switch (cv['align']) {
                        case 'center':
                            tx = cx + cw / 2;
                            break;
                        case 'left':
                            tx = cx + 10;
                            break;
                        case 'right':
                            tx = cx + cw - 10;
                            break;
                    }

                    var t_n = 0;
                    var t_lns = cv['display'].split('\n');
                    for (let t_ln of t_lns) {
                        ty = h - 5 - 18 * (t_lns.length - 0.5 - t_n);
                        ctx.fillText(t_ln, tx, ty);
                        t_n += 1;
                    }

                    ctx.font = '12px FontAwesome';
                    ctx.textAlign = 'right'

                    var t_icons = '';
                    if (this.filterdata.has(cv['key'])) {
                        t_icons += ' \uf0b0';
                    }
                    // this.sortselect={'key':k, 'az':az};
                    // U+25B2 U+25BC
                    if (this.sortselect && this.sortselect['key'] == cv['key']) {
                        if (['money', 'int'].includes(cv['type'])) {
                            t_icons += this.sortselect['az'] ? ' \uf162' : ' \uf163';
                        } else {
                            t_icons += this.sortselect['az'] ? ' \uf15d' : ' \uf15e';
                        }
                    }

                    // this.subtotalselect
                    if (this.subtotalselect && this.subtotalselect['key'] == cv['key']) {
                        t_icons += ' \uf0fe'; // f00b f0c9 f0fe
                    }

                    if (t_icons) {
                        ctx.fillText(t_icons, cx + cw - 10, 10);
                    }

                    break;

                case 'C':

                    ctx.font = '16px FontAwesome';
                    ctx.textAlign = 'right'
                    ctx.fillStyle = '#bbb'

                    ctx.fillText('\uf0b0 \uf15d', cx + cw - 10, 10);

                    ctx.strokeStyle = '#bbb';

                    ctx.beginPath();
                    ctx.lineWidth = 2;
                    ctx.moveTo(cx + cw - 45, 6);
                    ctx.lineTo(cx + cw - 8, 16);
                    ctx.stroke();
                    // ctx.beginPath();
                    // ctx.moveTo(cx + cw - 35, 11.5);
                    // ctx.lineTo(cx + cw - 10, 11.5);
                    // ctx.stroke();

                    break;
            }


        }


        ctx.restore()

    }


    draw_tbody(ctx, x, y, w, h) {

        ctx.save();
        ctx.translate(x, y);
        ctx.rect(0, 0, w, h);
        ctx.clip();

        ctx.fillStyle = "#FAFAFA";
        ctx.fillRect(0, 0, this.z_A_w, h);

        ctx.beginPath();
        ctx.strokeStyle = "#F0F0F0";
        ctx.moveTo(this.z_A_w - 0.5, 0);
        ctx.lineTo(this.z_A_w - 0.5, h);
        ctx.stroke();

        ctx.textBaseline = 'middle';
        ctx.fillStyle = "#444";
        ctx.strokeStyle = "#F0F0F0";

        var showdata = [];

        if (this.subtotalselect) {
            for (let i = 0; i < this.stdata.length; i++) {
                if (this.subtotaltype === 1) {
                    showdata.push(this.stdata[i]);
                    for (let d of this.istdata[i]) {
                        showdata.push(d);
                    }
                } else if (this.subtotaltype === 2) {
                    for (let d of this.istdata[i]) {
                        showdata.push(d);
                    }
                    showdata.push(this.stdata[i]);
                } else {
                    showdata.push(this.stdata[i]);
                }
            }
        } else {
            showdata = this.data;
        }

        var ln = 0;

        var by = parseInt(this.sprites[0].p * ((showdata.length + 1) * this.row_h - h));
        this.buttons = [];

        for (let i = 0; i < showdata.length; i++) {
            let dk = showdata[i];

            var d = (typeof dk === 'number') ? (this.fulldata[dk]) : (dk);
            var ly8 = (ln + 0) * this.row_h - by;
            var ly2 = (ln + 1) * this.row_h - by;
            if (ly2 < 0 || ly8 > h) {
                ln = ln + 1;
                continue;
            }

            if (this.subtotalselect) {
                if (typeof dk !== 'number') {
                    ctx.save();
                    if (this.subtotaltype === 0) {
                        if ((ln % 2) == 1) {
                            ctx.fillStyle = "#F4F4F4";
                        } else {
                            ctx.fillStyle = "#fff";
                        }
                    } else {
                        ctx.fillStyle = "#80CBC4";
                    }
                    ctx.fillRect(this.z_A_w, ly8, this.z_B_w, this.row_h);


                    ctx.strokeStyle = "#00695C";
                    if (this.subtotaltype === 1) {
                        ctx.beginPath();
                        ctx.moveTo(this.z_A_w, ly8 + 0.5);
                        ctx.lineTo(this.z_A_w + this.z_B_w, ly8 + 0.5);
                        ctx.stroke();
                    } else if (this.subtotaltype === 2) {
                        ctx.beginPath();
                        ctx.moveTo(this.z_A_w, ly2 - 0.5);
                        ctx.lineTo(this.z_A_w + this.z_B_w, ly2 - 0.5);
                        ctx.stroke();
                    }

                    ctx.restore();
                }
            } else {
                if ((ln % 2) == 1) {
                    ctx.save();
                    ctx.fillStyle = "#F4F4F4";
                    ctx.fillRect(this.z_A_w, ly8, this.z_B_w, this.row_h);
                    ctx.restore();
                }
            }

            if (this.rowselect.has(ln)) {

                ctx.save();
                // ctx.fillStyle = ((ln % 2) == 1) ? "#C1DFF8" : "#DBEFFF";
                ctx.fillStyle = "#C1DFF8";
                ctx.fillRect(this.z_A_w, ly8, this.z_B_w, this.row_h);
                ctx.restore();

                ctx.save();
                ctx.strokeStyle = "#99D1FF";
                if (!this.rowselect.has(ln - 1)) {
                    ctx.beginPath();
                    ctx.moveTo(this.z_A_w, ly8 + 0.5);
                    ctx.lineTo(this.z_A_w + this.z_B_w, ly8 + 0.5);
                    ctx.stroke();
                }
                if (!this.rowselect.has(ln + 1)) {
                    ctx.beginPath();
                    ctx.moveTo(this.z_A_w, ly2 - 0.5);
                    ctx.lineTo(this.z_A_w + this.z_B_w, ly2 - 0.5);
                    ctx.stroke();
                }
                ctx.restore();
            }

            var ty = (ln + 0.5) * this.row_h - by;
            var tx;
            var t;

            var ct, cv, ci, cm, cx, cw;
            var boldFlag = false;
            if (d.qingsong_blod || typeof dk !== 'number') {
                boldFlag = true;
            } else if (d.ratio == 0) {
                ctx.save();
                var pattern = ctx.createPattern(window.highpattern, "repeat");
                ctx.fillStyle = pattern;
                // ctx.fillStyle = ((ln % 2) == 1) ? "#C1DFF8" : "#DBEFFF";
                ctx.fillRect(this.z_A_w, ly8, this.z_B_w, this.row_h);
                ctx.restore();
            }
            // if (typeof dk !== 'number') {
            //     ctx.font = 'bold ' + this.z_stB_font;
            // }
            for (let [ct, cv, ci, cm, cx, cw] of this.cols) {
                ctx.fillStyle = "#444444";
                switch (ct) {

                    case 'A':
                        // if (boldFlag) {break;}
                        if (this.subtotalselect && typeof dk !== 'number') {
                            ctx.font = 'bold ' + this.z_stA_st_font;
                            ctx.textAlign = 'right';
                            tx = cx + cw * 0.6;
                            ctx.fillText(ln + 1, tx, ty - 5);
                            ctx.font = this.z_stA_st_font;
                            ctx.textAlign = 'right';
                            tx = cx + cw - 5;
                            ctx.fillText('' + d['___inner_count'], tx, ty + 5);
                        } else {
                            ctx.font = this.z_stA_font;
                            ctx.textAlign = 'right';
                            tx = cx + cw - 15;
                            ctx.fillText(ln + 1, tx, ty);
                        }

                        break;

                    case 'B':

                        ctx.font = this.z_stB_font;

                        if (cv['type'] == 'button') {

                            if (d[cv['key']]) {

                                t = d[cv['key']] || '';
                                let mt = ctx.measureText(t);

                                switch (cv['align']) {
                                    case 'center':
                                        tx = parseInt(cx + cw / 2 - mt.width / 2);
                                        break;
                                    case 'left':
                                        tx = cx + 10 + 5;
                                        break;
                                    case 'right':
                                        tx = cx + cw - mt.width - 10 - 5;
                                        break;
                                }

                                ctx.save();
                                ctx.fillStyle = "#3879D9";
                                ctx.fillRect(tx - 10, ty - 12 / 2 - 10, mt.width + 20, 12 + 20);
                                this.buttons.push([x + tx - 10, y + ty - 12 / 2 - 10, mt.width + 20, 12 + 20, dk, cv['key']]);
                                ctx.fillStyle = "#FFFFFF";
                                ctx.textAlign = 'left';
                                ctx.fillText(t, tx, ty);
                                ctx.restore();

                            }

                        } else {

                            ctx.textAlign = cv['align'];

                            switch (cv['align']) {
                                case 'center':
                                    tx = cx + cw / 2;
                                    break;
                                case 'left':
                                    tx = cx + 10;
                                    break;
                                case 'right':
                                    tx = cx + cw - 10;
                                    break;
                            }

                            if (cv['type'] == 'money') {
                                t = (d[cv['key']] / 100).toFixed(2);
                                t = t.replace(this.money_re, "$1,");
                            } else if (d[cv['key']] instanceof Set) {
                                if (d[cv['key']].size == 1) {
                                    t = '' + (d[cv['key']].values().next().value);
                                } else {
                                    ctx.font = this.z_stB_st_font;
                                    t = '' + (d[cv['key']].size)
                                    t = t.padStart(3) + ' 种';
                                }
                            } else {
                                t = '' + (d[cv['key']]);
                            }
                            // if (cv['watch']) { // 系数是str
                            //     const a = cv['watch'];
                            //     let b = 0;
                            //     if (cv['type'] == 'money') {
                            //         b = (d[cv['key']] / 100).toFixed(2)
                            //     } else {
                            //         b = d[cv['key']]
                            //     }
                            //     if (!isNaN(b) && a(b)) {
                            //         ctx.save();
                            //         ctx.fillStyle = "#FFCCCC";
                            //         ctx.fillRect(cx, ly8, cw, this.row_h);
                            //         ctx.restore();
                            //     }
                            // } else if (['money', 'int'].includes(cv['type']) && d[cv['key']] < 0) {
                            //     ctx.save();
                            //     ctx.fillStyle = "#FFCCCC";
                            //     ctx.fillRect(cx, ly8, cw, this.row_h);
                            //     ctx.restore();
                            // }
                            if (boldFlag) {
                                ctx.font = 'bold ' + this.z_stB_font;
                                ctx.fillStyle = "#000000";

                                // ctx.restore();
                            } else {
                                ctx.fillStyle = "#444444";

                            }
                            if (cv['watch']) { // 系数是str
                                const a = cv['watch'];
                                let b = 0;
                                if (cv['type'] == 'money') {
                                    b = (d[cv['key']] / 100).toFixed(2)
                                } else {
                                    b = d[cv['key']]
                                }
                                if (!isNaN(b) && a(b)) {
                                    ctx.fillStyle = "#ED1C24";
                                }
                            } else if (['money', 'int'].includes(cv['type']) && d[cv['key']] < 0) {
                                ctx.fillStyle = "#ED1C24";
                            }
                            // if (cv['watch']) { // 系数是str
                            //     const a = cv['watch'];
                            //     let b = 0;
                            //     if (cv['type'] == 'money') {
                            //         b = (d[cv['key']] / 100).toFixed(2)
                            //     } else {
                            //         b = d[cv['key']]
                            //     }
                            //     if (!isNaN(b) && a(b)) {
                            //         ctx.save();
                            //         ctx.fillStyle = "#FFCCCC";
                            //         ctx.fillRect(cx, ly8, cw, this.row_h);
                            //         ctx.restore();
                            //     }
                            // } else if (['money', 'int'].includes(cv['type']) && d[cv['key']] < 0) {
                            //     ctx.save();
                            //     ctx.fillStyle = "#FFCCCC";
                            //     ctx.fillRect(cx, ly8, cw, this.row_h);
                            //     ctx.restore();
                            // }
                            ctx.fillText(t, tx, ty);

                        }
                        break;
                }

            }

            ln = ln + 1;

        }

        ctx.restore();

        return;
    }

    draw_scrollarrow(ctx, w, h, o) {
        ctx.save();
        ctx.translate(w, h);
        ctx.beginPath();
        ctx.moveTo(0, -3 * o);
        ctx.lineTo(-5, 3 * o);
        ctx.lineTo(5, 3 * o);
        ctx.closePath();
        ctx.fill();
        ctx.restore();
    }

    draw_scroll(ctx, x, y, w, h) {
        ctx.save();
        ctx.translate(x, y);

        ctx.fillStyle = "#F1F1F1";
        ctx.fillRect(30 + 1, 0, 20 - 2, h);

        ctx.fillStyle = "#888";
        this.draw_scrollarrow(ctx, 40, 10, 1);
        this.draw_scrollarrow(ctx, 40, h - 10 - 50, -1);
        this.draw_scrollarrow(ctx, 40, h - 10 - 3 - 25, 1);
        this.draw_scrollarrow(ctx, 40, h - 10 + 3 - 25, 1);
        this.draw_scrollarrow(ctx, 40, h - 10 - 3, -1);
        this.draw_scrollarrow(ctx, 40, h - 10 + 3, -1);

        //this.scroll_cursor_h = 30;
        //this.draw_scroll_cursor(ctx,30,30,20,h-60);

        var showdata = [];

        if (this.subtotalselect) {
            for (let i = 0; i < this.stdata.length; i++) {
                if (this.subtotaltype === 1) {
                    showdata.push(this.stdata[i]);
                    for (let d of this.istdata[i]) {
                        showdata.push(d);
                    }
                } else if (this.subtotaltype === 2) {
                    for (let d of this.istdata[i]) {
                        showdata.push(d);
                    }
                    showdata.push(this.stdata[i]);
                } else {
                    showdata.push(this.stdata[i]);
                }
            }
        } else {
            showdata = this.data;
        }

        var sH = showdata.length * this.row_h;
        if (sH <= h) {
            h = sH;
        } else {
            ctx.scale(1, h / sH);
        }

        var by = parseInt(this.sprites[0].p * ((showdata.length + 1) * this.row_h - h));

        ctx.fillStyle = "#CCE8FF";
        ctx.fillRect(0, by, 30, h);

        ctx.restore();


        ctx.save();
        ctx.translate(x, y);
        ctx.scale(1, h / showdata.length);

        //ctx.fillStyle=(this.data.length>(h/3))?"#FF9966":"rgba(255,153,102,0.6)";
        ctx.fillStyle = (showdata.length > (h / 3)) ? "#FF9966" : "#FDBFA1";

        var ln = 0;
        var iww = (w - 20 - 5 - 1) / this.watchcols.length;
        for (let di = 0; di < showdata.length; di++) {
            let dk = showdata[di];
            var d = (typeof dk === 'number') ? (this.fulldata[dk]) : (dk);

            var cl = 0;
            for (let col of this.watchcols) {
                if (d[col['key']] < 0) {
                    ctx.fillRect(5 + iww * cl, ln, iww, 1);
                }
                cl += 1;
            }

            ln += 1;

        }

        ctx.restore();


        ctx.save();
        ctx.translate(x, y);

        ctx.strokeStyle = "#99D1FF";
        ctx.strokeRect(0.5, by * h / sH, 29, h * h / sH);

        ctx.restore();

    }

    draw_tfoot(ctx, x, y, w, h) {
        var rowcount = 3;
        if (this.isnotfoot) {
            rowcount = 1;
        }
        ctx.save();
        ctx.translate(x, y);

        ctx.fillStyle = "#FAFAFA";
        ctx.fillRect(0, 0, this.canvasWidth, h);

        if (this.rowselect.size > 0) {
            ctx.fillStyle = "#3879D9"; //#0066BB #DBEFFF
            ctx.fillRect(0, 0, this.canvasWidth, h / rowcount);
        }

        for (var i = 0; i < rowcount; i++) {
            ctx.beginPath();
            ctx.strokeStyle = "#F0F0F0";
            var ly = i * h / rowcount;
            ctx.moveTo(0, ly + 0.5);
            ctx.lineTo(this.canvasWidth, ly + 0.5);
            ctx.stroke();
        }

        ctx.font = '14px 微软雅黑';
        ctx.textBaseline = 'middle';


        var ct, cv, ci, cm, cx, cw;
        var tx, ty, t, d, t0;

        var ln;
        for (ln = 0; ln < rowcount; ln++) {

            ctx.fillStyle = "#444";

            ty = (h / rowcount) * (ln + 0.5);
            if (this.rowselect.size > 0) {
                d = [this.sumselectdata, this.sumdata, this.totaldata][ln];
                t0 = ['选择', '累计', '总共'][ln];
                if (ln == 0) {
                    ctx.fillStyle = "#ffffff";
                }
            } else {
                if (this.isnotfoot) {
                    var data = {};
                    for (var s in this.sumdata) {
                        if (s) { data[s] = 0; }
                    }
                    d = data;
                    t0 = '选择';
                } else {
                    d = [this.sumdata, this.propdata, this.totaldata][ln];
                    t0 = ['累计', '占比', '总共'][ln];
                }
            }

            for (let [ct, cv, ci, cm, cx, cw] of this.cols) {

                ctx.beginPath();
                ctx.strokeStyle = "#F0F0F0";
                ctx.moveTo(cx + cw - 0.5, 0);
                ctx.lineTo(cx + cw - 0.5, h);
                ctx.stroke();

                switch (ct) {

                    case 'A':

                        ctx.font = this.z_stB_font;
                        ctx.textAlign = 'right';
                        tx = cx + cw - 10;
                        ctx.fillText(t0, tx, ty);

                        break;

                    case 'B':

                        ctx.font = this.z_stB_font;

                        ctx.textAlign = cv['align'];

                        switch (cv['align']) {
                            case 'center':
                                tx = cx + cw / 2;
                                break;
                            case 'left':
                                tx = cx + 10;
                                break;
                            case 'right':
                                tx = cx + cw - 10;
                                break;
                        }

                        if (ln == 1 && this.rowselect.size == 0) {

                            t = '' + d[cv['key']];

                        } else {
                            if (cv['type'] == 'money') {

                                t = (d[cv['key']] / 100).toFixed(2);
                                t = t.replace(this.money_re, "$1,");

                            } else if (cv['type'] == 'int') {

                                t = '' + d[cv['key']];

                            } else if (cv['type'] == 'button') {

                                t = '';

                            } else {

                                t = '' + d[cv['key']] + '种';

                            }
                        }

                        if (ctx.measureText(t).width + 20 > cw) {
                            ctx.font = this.z_stB_micro_font;
                        }

                        if (ctx.measureText(t).width + 20 > cw) {
                            ctx.font = this.z_stB_mini_font;
                            switch (cv['align']) {
                                case 'center':
                                    tx = cx + cw / 2;
                                    break;
                                case 'left':
                                    tx = cx + 5;
                                    break;
                                case 'right':
                                    tx = cx + cw - 5;
                                    break;
                            }
                        }

                        ctx.fillText(t, tx, ty);

                        break;
                }

            }

        }

        ctx.restore();
    }

    onDblClick_sB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        if (this.subtotalselect && this.subtotaltype === 0) { return; }

        var dy = y - ry;

        var ln = 0;


        var showdata = [];

        if (this.subtotalselect) {
            for (let i = 0; i < this.stdata.length; i++) {
                if (this.subtotaltype === 1) {
                    showdata.push(this.stdata[i]);
                    for (let d of this.istdata[i]) {
                        showdata.push(d);
                    }
                } else if (this.subtotaltype === 2) {
                    for (let d of this.istdata[i]) {
                        showdata.push(d);
                    }
                    showdata.push(this.stdata[i]);
                } else {
                    showdata.push(this.stdata[i]);
                }
            }
        } else {
            showdata = this.data;
        }

        var by = parseInt(this.sprites[0].p * ((showdata.length + 1) * this.row_h - rh));

        for (let dk of showdata) {
            if (typeof dk === 'number') {
                var d = this.fulldata[dk];

                var ly8 = (ln + 0) * this.row_h - by;
                var ly2 = (ln + 1) * this.row_h - by;

                if (dy >= ly8 && dy <= ly2) {
                    if (this.onrunselect) {
                        safePromiseEval(this.onrunselect, { 'data': d });
                    }
                    break;
                }
            }
            ln += 1;
        }

        return;
    }

    onClick_sB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.y = y;
        this.ry = ry;
        this.rh = rh;
        if (!this.subtotalselect) {

            for (let [xx, yy, w, h, dk, bk] of this.buttons) {
                if (x > xx && x < xx + w && y > yy && y < yy + h) {
                    var d = this.fulldata[dk];
                    safePromiseEval(this.onrunselect, { 'data': d, 'button': bk });
                    return;
                }
            }

        }

        var dy = y - ry;

        // var showdata = (this.subtotalselect) ? (this.stdata) : (this.data);

        var sdlen = 0;
        if (this.subtotalselect) {
            if (this.subtotaltype === 0) {
                sdlen = this.stdata.length + 1;
            } else {
                sdlen = this.stdata.length + this.data.length + 1;
            }
        } else {
            sdlen = this.data.length + 1;
        }

        var by = parseInt(this.sprites[0].p * (sdlen * this.row_h - rh));

        var ln = 0;
        for (; ln < sdlen - 1; ln += 1) {

            var ly8 = (ln + 0) * this.row_h - by;
            var ly2 = (ln + 1) * this.row_h - by;

            if (dy >= ly8 && dy <= ly2) {
                break;
            }

        }
        var showdata = [];

        if (this.subtotalselect) {
            for (let i = 0; i < this.stdata.length; i++) {
                if (this.subtotaltype === 1) {
                    showdata.push(this.stdata[i]);
                    for (let d of this.istdata[i]) {
                        showdata.push(d);
                    }
                } else if (this.subtotaltype === 2) {
                    for (let d of this.istdata[i]) {
                        showdata.push(d);
                    }
                    showdata.push(this.stdata[i]);
                } else {
                    showdata.push(this.stdata[i]);
                }
            }
        } else {
            showdata = this.data;
        }
        if ((typeof showdata[ln] === 'number') || this.subtotaltype === 0) {
            this.rowselect = new Set([ln]);

            // safePromiseEval(this.onrunselect, { 'data': this.fulldata[showdata[ln]] });

            this.dropdown.style['display'] = 'none';

            this.calcSelectData();
            this.redraw();
        }

        // console.log(this.fulldata[showdata[ln]])
        // 点击复制
        if (this.fulldata[showdata[ln]]) {
            if (this.OnClick) {
                let aa = this.fulldata[showdata[ln]]
                console.log(aa);
                safePromiseEval(this.OnClick, { data: this.fulldata[showdata[ln]] });
                // this.OnClick(this.fulldata[showdata[ln]]);
            }
            var copyValue = this.fulldata[showdata[ln]][cv.key];


            if (cv.type === 'money') {
                copyValue = (copyValue / 100).toFixed(2);
            }
            const aux = document.createElement('input');
            aux.setAttribute('value', copyValue);
            document.body.appendChild(aux);
            aux.select();
            document.execCommand('copy');
            document.body.removeChild(aux);
        }

        return;
    }
    copyTableFoot(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        const Y_axis = this.canvasHeight - y;
        if (!cv.key) { return }
        let copyValue = '';
        if (Y_axis < 30) {
            //console.log('总共');
            copyValue = this.totaldata[cv.key];
        } else if (Y_axis < 60) {
            //console.log('占比或累计');
            if (this.rowselect.size > 0) {
                copyValue = this.sumdata[cv.key];
            } else {
                copyValue = this.propdata[cv.key];
            }
        } else if (Y_axis < 90) {
            //console.log('累计或选择');
            if (this.rowselect.size > 0) {
                copyValue = this.sumselectdata[cv.key];
            } else {
                copyValue = this.sumdata[cv.key];
            }
        }
        console.log(copyValue);
        if (cv.type === 'money' && typeof copyValue === 'number') {
            copyValue = (copyValue / 100).toFixed(2);
        }
        const aux = document.createElement('input');
        aux.setAttribute('value', copyValue);
        document.body.appendChild(aux);
        aux.select();
        document.execCommand('copy');
        document.body.removeChild(aux);
    }

    onRClick_sB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {

        var dy = y - ry;

        // var showdata = (this.subtotalselect) ? (this.stdata) : (this.data);

        var sdlen = 0;
        if (this.subtotalselect) {
            if (this.subtotaltype === 0) {
                sdlen = this.stdata.length + 1;
            } else {
                sdlen = this.stdata.length + this.data.length + 1;
            }
        } else {
            sdlen = this.data.length + 1;
        }

        var by = parseInt(this.sprites[0].p * (sdlen * this.row_h - rh));

        var ln = 0;
        for (; ln < sdlen - 1; ln += 1) {

            var ly8 = (ln + 0) * this.row_h - by;
            var ly2 = (ln + 1) * this.row_h - by;

            if (dy >= ly8 && dy <= ly2) {
                break;
            }

        }
        var showdata = [];

        if (this.subtotalselect) {
            for (let i = 0; i < this.stdata.length; i++) {
                if (this.subtotaltype === 1) {
                    showdata.push(this.stdata[i]);
                    for (let d of this.istdata[i]) {
                        showdata.push(d);
                    }
                } else if (this.subtotaltype === 2) {
                    for (let d of this.istdata[i]) {
                        showdata.push(d);
                    }
                    showdata.push(this.stdata[i]);
                } else {
                    showdata.push(this.stdata[i]);
                }

            }
        } else {
            showdata = this.data;
        }

        if ((typeof showdata[ln] === 'number') || this.subtotaltype === 0) {
            if (this.rowselect.has(ln)) {
                this.rowselect.delete(ln);
            } else {
                this.rowselect.add(ln);
            }
            this.dropdown.style['display'] = 'none';

            this.calcSelectData();
            this.redraw();
        }



        return;

    }
    onClick_rA(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        // 自定义排序
        if (this.subtotalselect) { return; }
        var box = this.dropdownSort.querySelector('.rds_selectbox');
        var opts = '<option value =""></option>';
        var ckeys = []
        for (let c of this.coldata) {
            if (c.type !== 'button') {
                ckeys.push(c.key);
                opts += '<option value ="' + c.key + '">' + c.display + '</option>';
            }
        }
        var selects = '';
        for (let count = 0; count < 4; count++) {
            selects += '<div style="padding: 4px; padding-left:0px"><select class="rds_select_col">' + opts + '</select><select class="rds_select_sort"><option value =""></option><option value ="u">升序</option><option value ="d">降序</option></select></div>';
        }
        box.innerHTML = selects;

        var selectcols = box.querySelectorAll('select.rds_select_col');
        var sortFuns = box.querySelectorAll('select.rds_select_sort');

        // this.selectSortCols = [];
        for (var i = 0; i < this.selectSortCols.length; i++) {
            var ssc = this.selectSortCols[i];
            for (var j = 0; j < ckeys.length; j++) {
                if (ssc.key === ckeys[j]) {
                    selectcols[i].options[j + 1].selected = true;
                }
            }
            if (ssc.az === 'u') {
                sortFuns[i].options[1].selected = true;
            } else if (ssc.az === 'd') {
                sortFuns[i].options[2].selected = true;
            }
        }
        this.dropdown.style['display'] = 'none';
        this.dropdownSort.style['display'] = 'block';
        this.dropdownSort.style['left'] = '0';
        this.dropdownSort.style['top'] = (ry + rh) + 'px';
    }
    onClick_rB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.dropdownSort.style['display'] = 'none';
        this.dropdown.setAttribute('colobject', cv['key']);

        this.dropdown.querySelector('input').value = '';

        var ston = this.dropdown.querySelector('.rdg_subtotal');
        ston.style['display'] = (cv['type'] == 'int' || cv['type'] == 'money') ? 'none' : 'block';

        var absoup = this.dropdown.querySelector('.rdg_absolute_up');
        var absodo = this.dropdown.querySelector('.rdg_absolute_down');
        absoup.style['display'] = (cv['type'] == 'int' || cv['type'] == 'money') ? 'block' : 'none';
        absodo.style['display'] = (cv['type'] == 'int' || cv['type'] == 'money') ? 'block' : 'none';

        var stoff = this.dropdown.querySelector('.rdg_unsubtotal');
        stoff.style['display'] = 'none';
        if (this.subtotalselect && this.subtotalselect['key'] === cv['key']) {
            stoff.style['display'] = 'block';
            ston.style['display'] = 'none';
        }


        var box = this.dropdown.querySelector('.rdg_selectbox');
        var opts = this.optiondata[cv['key']];

        var nfilter = this.filterdata.get(cv['key']);
        if (nfilter == null) {
            nfilter = [];
        }
        opts = opts.map(a => '<div><input type="checkbox" ' + (nfilter.includes(a) ? '' : 'checked') + '/><span>' + a + '</span></div>')
        opts.reverse();
        box.innerHTML = opts.join('');

        this.dropdown.style['display'] = 'block';
        var dw = this.dropdown.clientWidth;

        if (cx + dw > this.canvasWidth - this.z_C_w) {
            this.dropdown.style['left'] = 'auto';
            this.dropdown.style['right'] = (this.canvasWidth - (cx + cw)) + 'px';
        } else {
            this.dropdown.style['left'] = cx + 'px';
            this.dropdown.style['right'] = 'auto';
        }
        this.dropdown.style['min-width'] = cw + 'px';
        this.dropdown.style['top'] = (ry + rh) + 'px';

        return;
    }

    // 右上角 取消筛选条件
    onClick_rC(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.sortselect = null;
        this.subtotalselect = null;
        this.selectSortCols = [];
        this.filterdata = new Map();
        this.rowselect = new Set();
        // this.fulldata = Object.assign({},this.fulldataBAK); // 数字
        this.data = Array.from(new Array(this.fulldata.length), (val, index) => index);
        this.dropdown.style['display'] = 'none';

        this.sumdata = this.totaldata;
        this.calcProportionData();
        this.redraw();

    }

    onRClick_rC(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.rowselect = new Set();

        this.dropdown.style['display'] = 'none';

        this.redraw();

    }

    onClick_sC(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        var yy = y - ry;
        var xx = x - cx;

        var sdlen = 0;
        if (this.subtotalselect) {
            if (this.subtotaltype === 0) {
                sdlen = this.stdata.length + 1;
            } else {
                sdlen = this.stdata.length + this.data.length + 1;
            }
        } else {
            sdlen = this.data.length + 1;
        }
        var sdheight = sdlen * this.row_h;

        if (xx < cw - 20 && sdheight > this.z_s_h) {
            this.sprites[0].setP(yy / this.z_s_h);
            return;
        }

        if (yy < 20) {
            this.sprites[0].setP(this.sprites[0].p - (3 / sdlen));
            return;
        }

        if (yy > 20 && yy < rh - 50 - 20) {
            if (y < this.sprites[0].y) {
                this.sprites[0].setP(this.sprites[0].p - (this.z_s_h / sdheight));
                return;
            }
            if (y > this.sprites[0].y2) {
                this.sprites[0].setP(this.sprites[0].p + (this.z_s_h / sdheight));
                return;
            }
        }

        if (yy > rh - 50 - 20 && yy < rh - 50) {
            this.sprites[0].setP(this.sprites[0].p + (3 / sdlen));
            return;
        }

        if (yy > rh - 25 - 20 && yy < rh - 25) {
            this.sprites[0].setP(this.sprites[0].p - (this.z_s_h / sdheight));
            return;
        }

        if (yy > rh - 20 && yy < rh) {
            this.sprites[0].setP(this.sprites[0].p + (this.z_s_h / sdheight));
            return;
        }

    }

    onWheel_sA(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y, delta) {
        this.onWheel_s(delta);
    }
    onWheel_sB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y, delta) {
        this.onWheel_s(delta);
    }
    onWheel_sC(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y, delta) {
        this.onWheel_s(delta);
    }

    onWheel_s(delta) {

        // var showdata = (this.subtotalselect) ? (this.stdata) : (this.data);

        var sdlen = 0;
        if (this.subtotalselect) {
            if (this.subtotaltype === 0) {
                sdlen = this.stdata.length + 1;
            } else {
                sdlen = this.stdata.length + this.data.length + 1;
            }
        } else {
            sdlen = this.data.length + 1;
        }
        this.sprites[0].setP(this.sprites[0].p - (5 / sdlen) * delta);
    }

    onClick_tC(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {

        if (y < this.canvasHeight - 30) return; // rh/3
        if (this.onexport) return;

        this.onexport = true;
        this.redraw();
        let opt = { 'filters': [{ 'name': 'CSV FILE', 'exts': '*.csv' }], 'filename': (window.exportFileName ? window.exportFileName : 'export.csv') };
        eui.saveFile(opt).then(resolve => this.exportFile(resolve), reject => this.exportEnd());
    }

    exportFile(fn) {
        var exportdata = [];
        var tempcoldata = JSON.parse(JSON.stringify(this.coldata));
        if (this.subtotalselect) {
            tempcoldata.unshift({
                align: "left",
                display: "",
                key: "subtotal_title",
                type: "str",
                w: 80,
                width: 76
            });
            for (let i = 0; i < this.stdata.length; i++) {
                let d = this.stdata[i];
                let dr = {}
                    // 普通分类汇总 导出一条时显示内容
                for (let k in d) {
                    if (d[k] instanceof Set) {
                        if (d[k].size == 1) {
                            dr[k] = '' + (d[k].values().next().value);
                        } else {
                            dr[k] = (d[k].size) + '种'
                                //dr[k] = dr[k].padStart(3) + ' 种'; // '  x种'
                        }
                    } else {
                        dr[k] = '' + d[k];
                    }
                }

                if (this.subtotaltype !== 0 && this.istdata[i].length === 1) {
                    dr = JSON.parse(JSON.stringify(this.fulldata[this.istdata[i][0]]));
                }
                dr.subtotal_title = '小计';

                if (this.subtotaltype === 1) {
                    exportdata.push(dr);
                    for (let c of this.istdata[i]) {
                        let opt = this.fulldata[c];
                        opt.subtotal_title = '';
                        let opt1 = {}
                        for (let i in opt) {
                            opt1[i] = opt[i]
                            if (!isNaN(opt[i])) {
                                opt1[i] = opt[i] === null ? '0' : opt[i].toString();
                            }
                        }
                        exportdata.push(opt1);
                    }
                } else if (this.subtotaltype === 2) {
                    for (let c of this.istdata[i]) {
                        let opt = this.fulldata[c];
                        opt.subtotal_title = '';
                        let opt1 = {}
                        for (let i in opt) {
                            opt1[i] = opt[i]
                            if (!isNaN(opt[i])) {
                                opt1[i] = opt[i] === null ? '0' : opt[i].toString();
                            }
                        }
                        exportdata.push(opt1);
                    }
                    exportdata.push(dr);
                } else {
                    exportdata.push(dr);
                }
            }
        } else {
            for (let dk of this.data) {
                let opt = this.fulldata[dk];
                let opt1 = {}
                for (let i in opt) {
                    opt1[i] = opt[i]
                    if (!isNaN(opt[i])) {
                        // opt1[i] = opt[i].toString()
                        opt1[i] = opt[i] === null ? '0' : opt[i].toString(); // null值没有
                    }
                }
                exportdata.push(opt1);
            }
        }
        const data = {};
        for (let cd of tempcoldata) {
            if (this.sumdata[cd.key]) {
                let t = '';
                if (cd['type'] == 'money' || cd['type'] == 'int') {
                    //t = (this.sumdata[cd['key']] / 100).toFixed(2);
                    //t = t.replace(this.money_re, "$1,");
                    t = '' + this.sumdata[cd['key']];
                } else if (cd['type'] == 'button') {
                    t = '';
                } else {
                    t = '' + this.sumdata[cd['key']] + '种';
                }
                data[cd.key] = t;
            } else {
                data[cd.key] = '0';
            }
        }
        // data['chain'] = ' ';
        exportdata.push(data);
        eui.exportSheet(fn, tempcoldata, exportdata).then(resolve => this.exportEnd());
    }

    exportEnd() {
        this.onexport = false;
        this.redraw();
    }

    onSort(az) {
        var k = this.dropdown.getAttribute('colobject');

        if (this.subtotalselect) {
            this.makeSubtotalsSort(k, az);
            // this.makeSort(k, az); // liwei注释
        } else {
            this.makeSort(k, az);
        }

        this.rowselect = new Set();

        this.sortselect = { 'key': k, 'az': az };
        this.dropdown.style['display'] = 'none';
        this.redraw();
    }

    makeSort(k, az) {
        var colinf = this.colmap.get(k);
        if (colinf['type'] === 'button') {
            return;
        }
        if (colinf['type'] === 'str') {
            this.data = this.data.sort((a, b) => {
                let av = '' + this.fulldata[a][k];
                let bv = '' + this.fulldata[b][k];
                return av.localeCompare(bv) * (az ? 1 : -1);

            });
            return;
        }
        this.data = this.data.sort((a, b) => {
            return (this.fulldata[a][k] - this.fulldata[b][k]) * (az ? 1 : -1);
        })
        return;
    }

    makeSortCols(cs) {
        var __this = this;
        var c = cs[0];
        var colinf = this.colmap.get(c.key);
        var sortaz = {};
        cs.forEach(c => {
            sortaz[c.key] = c.az;
        });
        this.fulldata.sort(function(a, b) {
            return __this.SortByProps2(a, b, sortaz);
        });
        this.data = Array.from(new Array(this.fulldata.length), (val, index) => index); // 如果直接排this.fulldata的话。
    }

    SortByProps2(item1, item2, propOrders) {
        var cps = []; // 用于记录各个排序属性的比较结果，-1 | 0 | 1 。
        var isAsc = true; // 排序方向。     
        for (var p in propOrders) {
            isAsc = propOrders[p] === "u";
            if (item1[p] > item2[p]) {
                cps.push(isAsc ? 1 : -1);
                break; // 可以跳出循环了，因为这里就已经知道 item1 “大于” item2 了。
            } else if (item1[p] === item2[p]) {
                cps.push(0);
            } else {
                cps.push(isAsc ? -1 : 1);
                break; // 可以跳出循环，item1 “小于” item2。
            }
        }
        for (var j = 0; j < cps.length; j++) {
            if (cps[j] === 1 || cps[j] === -1) {
                return cps[j];
            }
        }
        return false;
    }


    // 绝对值排序 liwei加
    onAbsoluteSort(az) {
        var k = this.dropdown.getAttribute('colobject');

        if (this.subtotalselect) {
            this.makeSubAbsoluteSort(k, az);
            // this.makeAbsoluteSort(k, az); // liwei注释
        } else {
            this.makeAbsoluteSort(k, az);
        }

        this.rowselect = new Set();

        this.sortselect = { 'key': k, 'az': az };
        this.dropdown.style['display'] = 'none';
        this.redraw();
    }

    makeAbsoluteSort(k, az) {

        var colinf = this.colmap.get(k);
        if (colinf['type'] === 'button') {
            return;
        }
        this.data = this.data.sort((a, b) => {
            return (Math.abs(this.fulldata[a][k]) - Math.abs(this.fulldata[b][k])) * (az ? 1 : -1);
        })
        return;
    }

    onSubtotals(sw) {
        if (sw === 3) {
            this.subtotalselect = null;
        } else {
            var k = this.dropdown.getAttribute('colobject');
            this.subtotalselect = { 'key': k };
            this.subtotaltype = sw;
            this.makeSubtotals(k);
        }


        this.rowselect = new Set();

        this.dropdown.style['display'] = 'none';
        this.redraw();
    }

    makeSubtotals(k) {
        var colinf = this.colmap.get(k);
        var stmap = {};
        for (let x of this.data) {
            let row = this.fulldata[x];
            let v = this.fulldata[x][k];
            if (!stmap[v]) stmap[v] = { '___inner_count': 0 };
            stmap[v]['___inner_count'] += 1;
            for (let c of this.coldata) {
                let kc = c['key'];
                if (c['type'] === 'button') {
                    stmap[v][kc] = null;
                } else if (c['type'] === 'str') {
                    if (!stmap[v][kc]) stmap[v][kc] = new Set();
                    stmap[v][kc].add(row[kc]);
                } else {
                    if (!stmap[v][kc]) stmap[v][kc] = 0;
                    stmap[v][kc] += row[kc];
                }
            }
        }
        this.stdata = [];
        this.istdata = [];

        for (let rk in stmap) {
            this.stdata = this.stdata.concat(stmap[rk]);
            if (this.subtotaltype !== 0) {
                let isc = [];
                for (let x of this.data) {
                    if (this.fulldata[x][k] === rk) {
                        isc.push(x);
                    }
                }
                this.istdata.push(isc);
            }
        }

        if (this.sortselect) {
            this.makeSubtotalsSort(this.sortselect['key'], this.sortselect['az']);
        }
    }

    makeSubtotalsSort(k, az) {

        var colinf = this.colmap.get(k);

        if (colinf['type'] === 'button') {
            return;
        }

        if (colinf['type'] === 'str') {
            this.stdata = this.stdata.sort((a, b) => {
                if (a[k].size == 1 && b[k].size == 1) {
                    let av = '' + a[k].values().next().value;
                    let bv = '' + b[k].values().next().value;
                    return av.localeCompare(bv) * (az ? 1 : -1);
                } else {
                    return (a[k].size - b[k].size) * (az ? 1 : -1);
                }
            });
            this.getSortIstdata();
            return;
        }

        this.stdata = this.stdata.sort((a, b) => {

            return (a[k] - b[k]) * (az ? 1 : -1);

        })
        this.getSortIstdata();

        return;
    }
    makeSubAbsoluteSort(k, az) {

            var colinf = this.colmap.get(k);

            if (colinf['type'] === 'button') {
                return;
            }

            this.stdata = this.stdata.sort((a, b) => {

                return (Math.abs(a[k]) - Math.abs(b[k])) * (az ? 1 : -1);

            })
            this.getSortIstdata();

            return;
        }
        // 排序，单独处理istdata
    getSortIstdata() {
        const key = this.subtotalselect.key;
        if (this.subtotaltype !== 0) {
            const newIstdata = [];
            for (let s of this.stdata) {
                let isc = [];
                for (let x of this.data) {
                    let v = this.fulldata[x][key];
                    if (v === s[key].values().next().value) {
                        isc.push(x);
                    }
                }
                newIstdata.push(isc);
            }

            this.istdata = newIstdata;
        }
    }

    onFilter() {

        this.data = Array.from(new Array(this.fulldata.length), (val, index) => index);
        if (this.sortselect) {
            this.makeSort(this.sortselect['key'], this.sortselect['az']);
        }

        var k = this.dropdown.getAttribute('colobject');
        var colinf = this.colmap.get(k);
        var box = this.dropdown.querySelector('.rdg_selectbox');
        let boxs = Array.from(box.children);
        boxs = boxs.filter(item => !item.firstElementChild.checked || item.offsetParent === null).map(item => item.innerText);
        if (boxs.length == 0) {
            this.filterdata.delete(k);
        } else {
            this.filterdata.set(k, boxs);
        }

        for (let [key, nfilter] of this.filterdata) {
            colinf = this.colmap.get(key);
            if (colinf['type'] == 'str') {
                if (colinf['dispose']) {
                    this.data = this.data.filter(a => (!nfilter.includes(('' + this.fulldata[a][key]).substr(0, 7))));
                } else {
                    this.data = this.data.filter(a => (!nfilter.includes('' + this.fulldata[a][key])));
                }

            } else {
                nfilter = nfilter.join('');
                if (nfilter == '负数') {
                    this.data = this.data.filter(a => (this.fulldata[a][key] >= 0))
                } else if (nfilter == '正数') {
                    this.data = this.data.filter(a => (this.fulldata[a][key] <= 0))
                } else if (nfilter == '0') {
                    this.data = this.data.filter(a => (this.fulldata[a][key] != 0))
                } else if (nfilter == '正数0') {
                    this.data = this.data.filter(a => (this.fulldata[a][key] < 0))
                } else if (nfilter == '正数负数') {
                    this.data = this.data.filter(a => (this.fulldata[a][key] == 0))
                } else if (nfilter == '0负数') {
                    this.data = this.data.filter(a => (this.fulldata[a][key] > 0))
                } else {
                    this.data = [];
                }
            }
        }

        if (this.subtotalselect) {
            this.makeSubtotals(this.subtotalselect['key']);
        }

        this.rowselectselect = new Set();

        this.dropdown.style['display'] = 'none';
        this.calcSumData();
        this.calcProportionData();
        this.redraw();
    }
    onSorter() {
        // 如果改复制fulldata排序，以后点击也是问题。
        // 如果直接改fulldata,不能清除筛选。
        // 获取自定义排序选择的值
        var box = this.dropdownSort.querySelector('.rds_selectbox');
        var selectcols = box.querySelectorAll('select.rds_select_col');
        var sortFuns = box.querySelectorAll('select.rds_select_sort');
        this.selectSortCols = [];
        var i = 0;
        for (var s of selectcols) {
            var cIndex = s.selectedIndex;
            var sIndex = sortFuns[i].selectedIndex;
            var key = s.options[cIndex].value;
            var fun = sortFuns[i][sIndex].value;
            if (!!key && !!fun) {
                this.selectSortCols.push({ key: key, az: fun });
            }
            i++;
        }
        console.log(this.selectSortCols);
        this.makeSortCols(this.selectSortCols);
        this.rowselect = new Set();
        this.dropdownSort.style['display'] = 'none';
        this.redraw();
    }

}


class StretchCheckGrid extends DataGrid {

    constructor() {
        super();
        this.prepare = [
            ['rowdata', 'rowdata'],
            ['format', 'dataformat']
        ];
        this.today = new Date();
        this.today.setHours(0);
        this.today.setMinutes(0);
        this.today.setSeconds(0);
        this.today.setMilliseconds(0);
        this.firstday = new Date(this.today);
        this.term = 200;
    }

    init(args) {

        this.rowdata = args['rowdata'];
        //this.today = new Date(args['lastdate']);
        this.today = new Date(this.getAttribute('lastdate'));

        this.month_count = 2;

        this.z_A_w = 25;
        this.z_B_w = 105;
        this.z_r_h = 40;
        this.z_u_h = 15;

        this.format = args['format'];

        this.areacls = { 'sD': 'chain_day', 'sC': 'chain_month', 'tD': 'zhongying_day', 'tC': 'zhongying_month' }

        this.fulldata = new Map();
        this.fetchapi = this.getAttribute('fetchdata');

        this.loadpattern = this.makePattern('#DDD', 5);
        //this.warnpattern = this.makePattern('#FF9F9F',3);

        this.select = null;
        this.rowsortmode = 0;
        this.rowsortmodenames = [
            '\uf005 \uf15d \uf042',
            '\uf15d \uf005 \uf042',
            '\uf042 \uf15d \uf005',
            '\uf042 \uf005 \uf15d',
        ];

        this.rowSort();

        this.innerHTML = `
    <canvas></canvas>
    <canvas></canvas>
    <canvas></canvas>
    `
    }

    clearData() {
        this.fulldata = new Map();
        this.layout();
    }

    rowSort() {
        switch (this.rowsortmode) {
            case 0:
                this.rowdata = this.rowdata.sort(function(a, b) {
                    if (a['star'] == b['star']) {
                        return a['pinyin'].localeCompare(b['pinyin']);
                    }
                    if (a['star']) { return -1; }
                    return 1;
                })
                break;
            case 1:
                this.rowdata = this.rowdata.sort((a, b) => (a['pinyin'].localeCompare(b['pinyin'])))
                break;
            case 2:
                this.rowdata = this.rowdata.sort(function(a, b) {
                    if (a['zone'] == b['zone']) {
                        return a['pinyin'].localeCompare(b['pinyin']);
                    }
                    if (a['zone'] == 1) { return -1; }
                    return 1;
                })
                break;
            case 3:
                this.rowdata = this.rowdata.sort(function(a, b) {
                    if (a['zone'] == b['zone']) {
                        if (a['star'] == b['star']) {
                            return a['pinyin'].localeCompare(b['pinyin']);
                        }
                        if (a['star']) { return -1; }
                        return 1;
                    }
                    if (a['zone'] == 1) { return -1; }
                    return 1;
                })
                break;
        }
    }

    makePattern(color, p) {
        var pattern = document.createElement('canvas');
        pattern.width = p;
        pattern.height = p;

        var pctx = pattern.getContext('2d');
        pctx.beginPath();
        pctx.strokeStyle = color;
        pctx.moveTo(p, 0);
        pctx.lineTo(0, p);
        pctx.stroke();

        return pattern;
    }

    layout() {

        this.z_st_h = this.canvasHeight - this.z_r_h - this.z_u_h;
        this.stdEm = this.z_st_h / (this.rowdata.length + 1.5);
        this.z_t_h = Math.round(this.stdEm * 1.5);
        this.z_s_h = this.z_st_h - this.z_t_h

        this.i_C_w = parseInt(Math.max(15, this.stdEm) * (this.format['chain_month'].length + 1));
        this.z_C_w = this.i_C_w * this.month_count;

        this.z_D_w = this.canvasWidth - this.z_A_w - this.z_B_w - this.z_C_w;
        this.day_count = parseInt(this.z_D_w / (Math.max(15, this.stdEm) * (this.format['chain_day'].length + 1)));

        this.rows = [];
        this.rows.push(['r', '', 0, 1, 0, this.z_r_h]);

        var i = 0;
        for (let [y, h] of divideByInteger(this.z_s_h, this.rowdata.length)) {
            this.rows.push(['s', this.rowdata[i], i, this.rowdata.length, this.z_r_h + y, h]);
            i += 1;
        }

        this.rows.push(['t', '中影', 0, 1, this.z_r_h + this.z_s_h, this.z_t_h]);
        this.rows.push(['u', '', 0, 1, this.z_r_h + this.z_s_h + this.z_t_h, this.z_u_h]);

        this.cols = [];
        var x = 0;
        this.cols.push(['A', '', 0, 1, 0, this.z_A_w]);
        x += this.z_A_w;
        this.cols.push(['B', '', 0, 1, x, this.z_B_w]);
        x += this.z_B_w;


        for (i = 0; i < this.month_count; i++) {
            let d = new Date(this.today);
            d.setMonth(this.today.getMonth() - this.month_count + i + 1);
            d.setHours(0);
            d.setMinutes(0);
            d.setSeconds(0);
            d.setMilliseconds(0);
            //let d_str = d.toLocaleDateString();
            this.cols.push(['C', d, i, this.month_count, x, this.i_C_w]);
            x += this.i_C_w;
        }

        i = 0;
        for (let [cx, cw] of divideByInteger(this.z_D_w, this.day_count)) {
            let d = new Date(this.today);
            d.setDate(this.today.getDate() - this.day_count + i + 1);
            d.setHours(0);
            d.setMinutes(0);
            d.setSeconds(0);
            d.setMilliseconds(0);
            //let d_str = d.toLocaleDateString();
            this.cols.push(['D', d, i, this.day_count, x, cw]);
            x += cw;
            i += 1;
        }

        for (let [ct, cv, ci, cm, cx, cw] of this.cols) {

            for (let rt of['r', 's', 't']) {
                let fetchtype = this.areacls[rt + ct];
                if (fetchtype) {
                    let d_str = cv.toLocaleDateString();
                    let args = { 'fetchtype': fetchtype, 'date': cv, 'strDate': d_str };
                    let k = '' + rt + ct + ':' + d_str;
                    if (!this.fulldata.has(k)) {
                        safePromiseEval(this.fetchapi, args).then(r => (this.fulldata.set(k, r) && this.redraw()));
                    }
                }
            }

        }

        this.sprites = [];
        var w = parseInt(this.z_D_w * this.day_count / this.term);
        this.sprites.push(new ScrollBarH(this, this.canvasWidth - this.z_D_w, this.z_r_h + this.z_s_h + this.z_t_h, this.z_D_w, this.z_u_h, w));
        this.sprites[0].x = this.canvasWidth - this.z_D_w * ((this.firstday - this.today) / (24 * 3600 * 1000)) / this.term - w;
    }

    sprite_dragEnd(s, x, y) {

        var d = new Date(this.firstday);
        var dx = this.term * (this.canvasWidth - s.x - s.w) / this.z_D_w;
        dx = parseInt(Math.round(dx));
        d.setDate(d.getDate() - dx);

        this.today = d;
        this.layout();
    }

    draw(deep) {
        if (deep == 2) {
            this.draw2(deep);
        }
        if (deep == 1) {
            this.draw1(deep);
        }
    }

    draw1(deep) {

        var ctx = this.layers[1].getContext('2d');

        var zwy = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'];
        var zwx = ['日', '一', '二', '三', '四', '五', '六'];

        let [rt, rv, ri, rm, ry, rh] = this.rows[this.rows.length - 1];

        ctx.font = '9px 微软雅黑';
        ctx.textBaseline = 'middle';


        ctx.fillStyle = "#FAFAFA";
        ctx.fillRect(0, ry, this.canvasWidth, rh);

        ctx.beginPath();
        //ctx.strokeStyle="#DDD";
        //ctx.moveTo( this.canvasWidth-this.z_D_w-0.5, ry );
        //ctx.lineTo( this.canvasWidth-this.z_D_w-0.5, ry+rh );
        ctx.fillStyle = "#EEE";
        ctx.fillRect(0, ry, this.canvasWidth - this.z_D_w, rh);
        ctx.stroke();

        ctx.beginPath();
        ctx.strokeStyle = "#DDD";
        ctx.moveTo(0, ry - 0.5);
        ctx.lineTo(this.canvasWidth, ry - 0.5);
        ctx.stroke();

        //ctx.fillStyle = "#B18900";
        //ctx.fillText( this.today.toLocaleDateString(), 4, ry+rh/2 );

        ctx.fillStyle = '#CECECE';
        ctx.fillRect(this.sprites[0].x, this.sprites[0].y, this.sprites[0].w, this.sprites[0].h);

        var d = new Date(this.firstday);
        var xx = 0;
        for (let i = 0; i < this.term; i++) {
            xx = this.canvasWidth - (this.z_D_w * i) / (this.term - 1);
            if (d.getDate() == 1) {
                ctx.beginPath();
                ctx.strokeStyle = "#444";
                ctx.moveTo(xx, ry + rh * 0.6);
                ctx.lineTo(xx, ry + rh);
                ctx.stroke();
                ctx.fillStyle = "#444";
                ctx.fillText(zwy[d.getMonth()] + '月', xx + 3, ry + rh / 2);
            }
            d.setDate(d.getDate() - 1);
        }


        ctx.shadowOffsetX = 2;
        ctx.shadowOffsetY = 2;
        ctx.shadowBlur = 4;
        ctx.shadowColor = "rgba(0, 0, 0, 0.2)"; //or use rgb(red, green, blue)

        xx = Math.min(this.sprites[0].x, this.canvasWidth - 105)

        ctx.fillStyle = "#fff";
        ctx.fillRect(xx, ry - 60, 100, 50);


        ctx.shadowOffsetX = 0;
        ctx.shadowOffsetY = 0;
        ctx.shadowBlur = 0;
        ctx.shadowColor = null;

        ctx.strokeStyle = "#bbb";
        ctx.strokeRect(xx - 0.5, ry - 60 - 0.5, 100, 50);

        d = new Date(this.firstday);
        var dx = this.term * (this.canvasWidth - this.sprites[0].x - this.sprites[0].w) / this.z_D_w;
        dx = parseInt(Math.round(dx));
        d.setDate(d.getDate() - dx);

        ctx.font = 'bold 14px 微软雅黑';
        ctx.textAlign = 'center';
        ctx.fillStyle = "#555";
        ctx.fillText(d.toLocaleDateString(), xx + 50, ry - 10 - 15);
        d.setDate(d.getDate() - this.day_count);
        ctx.fillText(d.toLocaleDateString(), xx + 50, ry - 60 + 15);

    }


    draw2(deep) {

        var ctx = this.layers[2].getContext('2d');

        var zwy = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'];
        var zwx = ['日', '一', '二', '三', '四', '五', '六'];

        for (let [ct, cv, ci, cm, cx, cw] of this.cols) {

            if (ct == 'A') {
                ctx.fillStyle = "#FAFAFA";
                ctx.fillRect(cx, 0, cw, this.canvasHeight);
                ctx.fillStyle = "#F6F6F6";
                ctx.fillRect(cx, 0, cw, this.canvasHeight - this.z_t_h - this.z_u_h);
            }

            if (ct == 'B') {
                ctx.fillStyle = "#FAFAFA";
                ctx.fillRect(cx, 0, cw, this.canvasHeight);
            }

            if (ct == 'C') {
                ctx.fillStyle = "#FAFFFA";
                ctx.fillRect(cx, 0, cw, this.canvasHeight);

                if (!this.fulldata.has('sC:' + cv.toLocaleDateString())) {
                    var pattern = ctx.createPattern(this.loadpattern, "repeat");
                    ctx.fillStyle = pattern;
                    ctx.fillRect(cx, 0, cw, this.canvasHeight);
                }
            }

            if (ct == 'D') {

                if ([0, 6].includes(cv.getDay())) {
                    ctx.fillStyle = "#FFFAFA";
                    ctx.fillRect(cx, 0, cw, this.canvasHeight);
                }

                if (!this.fulldata.has('sD:' + cv.toLocaleDateString())) {
                    var pattern = ctx.createPattern(this.loadpattern, "repeat");
                    ctx.fillStyle = pattern;
                    ctx.fillRect(cx, 0, cw, this.canvasHeight);
                }
            }

            if (this.select && ct == this.select[0] && ci == this.select[1]) {
                ctx.fillStyle = "#f0f9ff";
                ctx.fillRect(cx, 0, cw, this.canvasHeight);
            }
        }

        for (let [rt, rv, ri, rm, ry, rh] of this.rows) {

            if (this.select && rt == this.select[4] && ri == this.select[5]) {
                ctx.fillStyle = "#d2eeff";
                ctx.fillRect(this.z_A_w + this.z_B_w, ry, this.canvasWidth, rh);
                //ctx.fillRect( this.select[2], ry, this.select[3], rh );
            }


            if (rt == 'r') {
                ctx.fillStyle = "#FAFAFA";
                ctx.fillRect(0, 0, this.canvasWidth, rh);

                ctx.fillStyle = "#D1F9D1";
                ctx.fillRect(this.z_A_w + this.z_B_w, 0, this.z_C_w, rh);

                ctx.beginPath();
                ctx.strokeStyle = "#CCC";
                ctx.moveTo(0, ry + rh - 0.5);
                ctx.lineTo(this.canvasWidth, ry + rh - 0.5);
                ctx.stroke();

            }

            if (rt == 's' && ri + 1 != rm) {
                ctx.beginPath();
                ctx.strokeStyle = "#E4E4E4";
                ctx.moveTo(0, ry + rh - 0.5);
                ctx.lineTo(this.z_A_w + this.z_B_w, ry + rh - 0.5);
                ctx.stroke();
                ctx.beginPath();
                ctx.strokeStyle = "#F0F0F0";
                if (this.select && rt == this.select[4] && (ri == this.select[5] || ri == this.select[5] - 1)) {
                    ctx.strokeStyle = "#50bdff";
                }
                ctx.moveTo(this.z_A_w + this.z_B_w, ry + rh - 0.5);
                ctx.lineTo(this.canvasWidth, ry + rh - 0.5);
                ctx.stroke();
            }

            if (rt == 't') {
                ctx.beginPath();
                ctx.strokeStyle = "#F0A0C0";
                ctx.moveTo(0, ry + 0.5);
                ctx.lineTo(this.canvasWidth, ry + 0.5);
                ctx.stroke();
            }

            ctx.font = '12px 微软雅黑';
            ctx.textBaseline = 'middle';
            ctx.fillStyle = "#555";
            ctx.textAlign = 'right';

            if (rt == 's') {
                ctx.fillText(rv['chain'], this.z_A_w + this.z_B_w - 5, ry + rh / 2);
            }

            if (rt == 't') {
                ctx.fillText(rv, this.z_A_w + this.z_B_w - 5, ry + rh / 2);
            }

            ctx.font = '9px 微软雅黑';
            ctx.textBaseline = 'middle';
            ctx.fillStyle = "#555";
            ctx.textAlign = 'left';

            if (rt == 's') {
                ctx.fillText('-甲乙' [rv['zone']], 8, ry + rh / 2);
            }

            if (rt == 's' && rv['star']) {
                ctx.fillStyle = "#FF9F9F";
                ctx.fillRect(0, ry, 3, rh);
            }

            if (rt == 'u') {

                ctx.save();
                ctx.rect(0, ry, this.canvasWidth, rh);
                ctx.clip();
                ctx.fillStyle = "#EEE";
                ctx.fillRect(0, ry, this.canvasWidth, rh);

                ctx.shadowOffsetX = 2;
                ctx.shadowOffsetY = 1;
                ctx.shadowBlur = 4;
                ctx.shadowColor = "rgba(0, 0, 0, 0.2)"; //or use rgb(red, green, blue)

                ctx.fillStyle = "#FFF";
                ctx.fillRect(0, ry - 10, this.canvasWidth, 10);

                ctx.shadowOffsetX = 0;
                ctx.shadowOffsetY = 0;
                ctx.shadowBlur = 0;
                ctx.shadowColor = null;

                ctx.beginPath();
                ctx.strokeStyle = "#DDD";
                ctx.moveTo(0, ry - 0.5);
                ctx.lineTo(this.canvasWidth, ry - 0.5);
                ctx.stroke();

                ctx.beginPath();
                ctx.strokeStyle = "#DDD";
                ctx.moveTo(this.canvasWidth - this.z_D_w - 0.5, ry);
                ctx.lineTo(this.canvasWidth - this.z_D_w - 0.5, ry + rh);
                ctx.stroke();

                ctx.fillStyle = "#AAA"; //B18900
                ctx.fillText(this.today.toLocaleDateString(), 4, ry + rh / 2);

                //for ( let i=6, j=0; i>=2; i-=2, j++ ) {
                //  let xx = this.canvasWidth - this.z_D_w - 30 - j*35;
                for (let i = 2, j = 0; i <= 6; i += 2, j++) {
                    let xx = this.z_A_w + this.z_B_w + 10 + j * 45;
                    if (i == this.month_count) {

                        ctx.shadowOffsetX = 2;
                        ctx.shadowOffsetY = 1;
                        ctx.shadowBlur = 4;
                        ctx.shadowColor = "rgba(0, 0, 0, 0.2)"; //or use rgb(red, green, blue)

                        ctx.fillStyle = "#FFF";
                        ctx.fillRect(xx, ry, 40, rh - 2);
                        //ctx.strokeStyle = "#DDD";
                        //ctx.strokeRect( xx-15-0.5, ry-0.5, 30, rh-2 );

                        ctx.shadowOffsetX = 0;
                        ctx.shadowOffsetY = 0;
                        ctx.shadowBlur = 0;
                        ctx.shadowColor = null;

                    }
                    ctx.fillStyle = "#444"; //B18900
                    ctx.textAlign = 'center';
                    ctx.fillText('' + i, xx + 20, ry + rh * 0.4);
                }

                ctx.fillStyle = '#CECECE';
                ctx.fillRect(this.sprites[0].x, this.sprites[0].y, this.sprites[0].w, this.sprites[0].h);

                ctx.textAlign = 'left';

                var d = new Date(this.firstday);
                for (let i = 0; i < this.term; i++) {
                    let xx = this.canvasWidth - (this.z_D_w * i) / (this.term - 1);
                    if (d.getDate() == 1) {
                        ctx.beginPath();
                        ctx.strokeStyle = "#bbb"; //FFC90E
                        ctx.moveTo(xx, ry + rh * 0.6);
                        ctx.lineTo(xx, ry + rh);
                        ctx.stroke();
                        ctx.fillStyle = "#999"; //B18900
                        ctx.fillText(zwy[d.getMonth()] + '月', xx + 3, ry + rh / 2);
                    }
                    d.setDate(d.getDate() - 1);
                }

                ctx.restore();
            }

        }

        for (let [ct, cv, ci, cm, cx, cw] of this.cols) {

            if (ct == 'B') {
                ctx.font = '12px FontAwesome';
                ctx.textBaseline = 'middle';
                ctx.fillStyle = "#444";
                ctx.textAlign = 'right';

                ctx.fillText(this.rowsortmodenames[this.rowsortmode], cx + cw - 10, this.z_r_h - 10);
            }

            if (ct != 'A' && !(ct == 'D' && ci == cm - 1) && !(ct == 'C' && ci == cm - 1)) {

                ctx.beginPath();
                ctx.strokeStyle = (ci == cm - 1) ? "#BBB" : "#DDD";
                ctx.moveTo(cx + cw - 0.5, 0);
                ctx.lineTo(cx + cw - 0.5, this.z_r_h);
                ctx.stroke();

                ctx.beginPath();
                ctx.strokeStyle = (ci == cm - 1) ? "#DDD" : "#F0F0F0";
                if (this.select && ct == this.select[0] && (ci == this.select[1] || ci == this.select[1] - 1)) {
                    ctx.strokeStyle = "#50bdff";
                }
                ctx.moveTo(cx + cw - 0.5, this.z_r_h);
                ctx.lineTo(cx + cw - 0.5, this.canvasHeight - this.z_u_h);
                ctx.stroke();

            }

            ctx.font = '14px 微软雅黑';
            ctx.textBaseline = 'middle';
            ctx.fillStyle = "#444";
            ctx.textAlign = 'right';


            if (ct == 'D') {

                if (ci == 0) {
                    ctx.save();
                    ctx.rect(cx, 0, cw, this.canvasHeight);
                    ctx.clip();

                    ctx.shadowOffsetX = 3;
                    ctx.shadowOffsetY = 0;
                    ctx.shadowBlur = 4;
                    ctx.shadowColor = "rgba(0, 0, 0, 0.12)"; //or use rgb(red, green, blue)

                    ctx.fillStyle = "#000";
                    ctx.fillRect(cx - 10, 0, 10, this.canvasHeight - this.z_u_h);

                    ctx.shadowOffsetX = 0;
                    ctx.shadowOffsetY = 0;
                    ctx.shadowBlur = 0;
                    ctx.shadowColor = null;

                    ctx.restore()
                }

                if ([0, 6].includes(cv.getDay())) {
                    ctx.fillStyle = "#F44";
                }
                ctx.fillText(cv.getDate() + '日', cx + cw - 5, 10);

                ctx.textAlign = 'left';
                ctx.font = '9px 微软雅黑';

                if (cv.getDate() == 1 || ci == 0) {
                    ctx.fillText(zwy[cv.getMonth()] + '月', cx + 5, 10);
                } else {
                    ctx.fillText(zwx[cv.getDay()], cx + 10, 10);
                }
            }

            if (ct == 'C') {

                //if ( [0,6].includes( cv.getDay() ) ) {
                //    ctx.fillStyle="#F44";
                //}
                ctx.fillText(zwy[cv.getMonth()] + '月', cx + cw - 5, 10);

            }

            for (let [rt, rv, ri, rm, ry, rh] of this.rows) {

                let fetchtype = this.areacls[rt + ct];
                if (!fetchtype) { continue; }

                let fmt = this.format[fetchtype];
                if (!fmt) { continue }

                let k = '' + rt + ct + ':' + cv.toLocaleDateString();

                let cdata = this.fulldata.get(k);
                if (!cdata) { continue; }
                if (rt == 's') {
                    cdata = cdata[rv['chainid']];
                }
                if (!cdata) { continue; }


                let ii = 0;
                for (let ifmt of fmt) {
                    let ix = cx + (cw * (ii + 1)) / (fmt.length + 1);
                    let iy = (rt == 'r') ? (ry + rh - this.stdEm) : (ry + rh / 2);
                    let showtype = ifmt['show'];
                    let idata = cdata[ifmt['key']];
                    let idata_badge = cdata[ifmt['key'] + '-badge'];
                    idata_badge = idata_badge ? idata_badge : '';

                    if (idata) {

                        draw_symbol(ctx, showtype, ix, iy, this.stdEm, idata, idata_badge);

                    } else {

                        ctx.save();
                        ctx.translate(ix, iy);

                        ctx.fillStyle = 'rgba(0,0,0,0.06)';
                        ctx.beginPath();
                        ctx.arc(0, 0, 2, 0, 2 * Math.PI);
                        ctx.fill();

                        ctx.restore();
                    }

                    ii += 1
                }

            }

        }

    }

    onClick_stCD(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {

        this.select = [ct, ci, cx, cw, rt, ri, ry, rh];

        let fetchtype = this.areacls[rt + ct];
        let d_str = cv.toLocaleDateString();
        let k = '' + rt + ct + ':' + d_str;

        let cdata = this.fulldata.get(k);
        if (rt == 's' && cdata) {
            cdata = cdata[rv['chainid']];
        }

        if (!cdata) {
            cdata = {}
        }

        let args = {
            'col': { 'date': cv, 'datatype': (ct == 'C') ? 'month' : 'day', 'strDate': cv.toLocaleString() },
            'row': (rt == 't') ? { 'datatype': 'zhongying' } : Object.assign({ 'datatype': 'chain' }, rv),
            'data': cdata,
        }

        console.log(args);

        let onselect = this.getAttribute('onselect');

        if (onselect) {
            safePromiseEval(onselect, args);
        }

        this.redraw();

        return;
    }

    onClick_sC(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.onClick_stCD(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y);
    }

    onClick_sD(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.onClick_stCD(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y);
    }

    onClick_tC(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.onClick_stCD(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y);
    }

    onClick_tD(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.onClick_stCD(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y);
    }

    cancel_select() {

        this.select = null;

        let args = {
            'col': null,
            'row': null,
            'data': null,
        }

        let onselect = this.getAttribute('onselect');

        if (onselect) {
            safePromiseEval(onselect, args);
        }

        this.redraw();

        return;
    }

    onClick_sA(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.cancel_select();
    }

    onClick_tA(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.cancel_select();
    }

    onClick_sB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.cancel_select();
    }

    onClick_tB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.cancel_select();
    }

    onClick_rC(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.cancel_select();
    }

    onClick_rD(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.cancel_select();
    }

    onClick_rB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.rowsortmode = (this.rowsortmode + 1) % 4;
        this.rowSort();
        this.layout();
        this.cancel_select();
    }

    onDblClick_sA(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {

        rv['star'] = rv['star'] ? false : true;

        let args = {
            'row': Object.assign({ 'datatype': 'chain' }, rv),
            'result': rv['star'],
        }

        let onsetstar = this.getAttribute('onsetstar');

        if (onsetstar) {
            safePromiseEval(onsetstar, args);
        }

        this.rowSort();
        this.layout();
        this.cancel_select();
    }

    onClick_uC(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {

        for (let i = 2, j = 0; i <= 6; i += 2, j++) {
            let xx = this.z_A_w + this.z_B_w + 10 + j * 45;
            if (x > xx && x < xx + 40) {
                if (i == this.month_count) return;
                this.month_count = i;
                this.layout();
                this.redraw();
                return;
            }
        }

    }
}


class StretchDataGrid extends DataGrid {

    constructor() {
        super();
        this.prepare = [
            ['rowdata', 'rowdata'],
            ['coldata', 'coldata'],
            ['colformat', 'colformat'],
            ['datetab', 'datetab'],
            ['tabformat', 'tabformat'],
            ['lastrowmode', 'lastrowmode'],
        ];

        this.prepare2 = [
            ['fulldata', 'fetchdata'],
            ['zhongdata', 'fetchzhongying'],
        ];

        this.today = new Date();

        let Month = this.today.getMonth() - 1;
        this.today.setMonth(Month)
        this.today.setDate(1);
        this.today.setHours(0);
        this.today.setMinutes(0);
        this.today.setSeconds(0);
        this.today.setMilliseconds(0);

        this.firstday = new Date(this.today);
        this.firstday.setMonth(this.firstday.getMonth() + 1);
    }

    makePattern(color, p) {
        var pattern = document.createElement('canvas');
        pattern.width = p;
        pattern.height = p;

        var pctx = pattern.getContext('2d');
        pctx.beginPath();
        pctx.strokeStyle = color;
        pctx.moveTo(p, 0);
        pctx.lineTo(0, p);
        pctx.stroke();

        return pattern;
    }

    prepare_args(x) {
        let d_str = this.today.toLocaleDateString();
        x['date'] = this.today;
        x['strDate'] = d_str;
    }

    init(args) {

        this.loadpattern = this.makePattern('#DDD', 5);

        this.rowdata = args['rowdata'];
        this.coldata = args['coldata'];
        this.colformat = args['colformat'];
        this.datetab = args['datetab'];
        this.tabformat = args['tabformat'];
        this.lastrowmode = args['lastrowmode'];

        this.innerHTML = `
    <style scoped>
    .rdg_shadow {
      position: absolute;
      background-color: rgba(0,0,0,0.2);
      display: none;
      width: 100%;
      height: 100%;
    }
    .rdg_dropdown {
      border: 1px solid #eee; 
      position: absolute;
      display: none;
      background-color: #fff;
      box-shadow: 2px 2px 3px #888888;
      font-family: 微软雅黑;
      padding: 10px;
      left: 60px;
      top: 30px;
      box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
    }
    input[type=text] {
      width: 40px;
      text-align:right;
      border: 1px solid #ccc;
      margin-right: 2px;
      padding-right: 2px;
    }
    .rdg_left_year,.rdg_right_year{
      position: relative;
      width: 20px;
      height: 10px;
      display: inline-block;
      cursor: pointer;
    }
    .rdg_left_year:after ,.rdg_right_year:after{
      content: " ";
      display: block;
      width: 0px;
      height: 0px;
      position: absolute;
      top: 0;
      bottom: 0;
      margin: auto;
      left: 0;
      right: 0;
      border-top: 7px solid rgba(255,255,255,0);
      border-bottom: 7px solid rgba(255,255,255,0);
    }
    .rdg_left_year:after{
      border-right:10px solid #6b6b6b;
    }
    .rdg_right_year:after{
      border-left:10px solid #6b6b6b;
    }
    select{
    
      width: calc(100% - 50px);
    }
    table{
          margin: 10px auto;
    }
    table button{
      width: 100%;
      border: none;
      background: #CAE3FB;
      font-size: .8em;
      padding: .6em;
      cursor: pointer;
      border-radius: .2em;
      transition: background .2s;
    }
    button{
      cursor: pointer;
      border: none;
      padding: 3px;
    }
    .current{
      float: right;
    }
    </style>
    <canvas></canvas>
    <div class="rdg_shadow"></div>
    <div class="rdg_dropdown">
    <span class="rdg_left_year" onclick="this.parentElement.parentElement.left_year();" ></span>
    <select class="rdg_year">
    </select>
    <span class="rdg_right_year" onclick="this.parentElement.parentElement.right_year();" ></span>
     <table>
        <tbody>
          <tr>
            <td><button data-value="0" onclick="this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.gotoDate(1);">01</button></td>
            <td><button data-value="1" onclick="this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.gotoDate(2);">02</button></td>
            <td><button data-value="2" onclick="this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.gotoDate(3);">03</button></td>
            <td><button data-value="3" onclick="this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.gotoDate(4);">04</button></td>
          </tr>
          <tr>
            <td><button data-value="4" onclick="this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.gotoDate(5);">05</button></td>
            <td><button data-value="5" onclick="this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.gotoDate(6);">06</button></td>
            <td><button data-value="6" onclick="this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.gotoDate(7);">07</button></td>
            <td><button data-value="7" onclick="this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.gotoDate(8);">08</button></td>
          </tr>
          <tr>
            <td><button data-value="8" onclick="this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.gotoDate(9);">09</button></td>
            <td><button data-value="9" onclick="this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.gotoDate(12);">10</button></td>
            <td><button data-value="10" onclick="this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.gotoDate(11);">11</button></td>
            <td><button data-value="11" onclick="this.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement.gotoDate(12);">12</button></td>
          </tr>
        </tbody>
      </table>
     <button class="cancel" onclick="this.parentElement.parentElement.cancel();" >取消</button>
     <button class="current" onclick="this.parentElement.parentElement.gotoDate(false);" >当月</button>
    </div>
    `;

        this.shaddow = this.querySelector('div.rdg_shadow');
        this.dropdown = this.querySelector('div.rdg_dropdown');
        this.rdg_year = this.dropdown.querySelector('.rdg_year');
        for (let i = (new Date()).getFullYear() + 1; i > 2007; i--) {
            let y = document.createElement('option');
            y.text = i
            this.rdg_year.add(y, null)
        }

        this.tabsprites = [];
        this.z_A_w = 25;
        this.z_B_w = 105;
        this.z_r_h = 60;
        this.z_q_h = 0;
        if (this.tabformat) {
            this.z_r_h = 50;
            this.z_q_h = 30;
        }

        this.z_rC_font = '14px 微软雅黑';
        this.z_stC_font = '12px 微软雅黑';

        this.money_re = /(\d)(?=(\d{3})+\.)/g;

        this.fulldata = (args['fulldata'] ? args['fulldata'] : []);
        this.zhongdata = (args['zhongdata'] ? args['zhongdata'] : {});

        this._summaryOK = false;
        this.select = null;
        this.rowsortmode = 0;
        this.rowsortmodenames = [
            '\uf005 \uf15d \uf042',
            '\uf15d \uf005 \uf042',
            '\uf042 \uf15d \uf005',
            '\uf042 \uf005 \uf15d',
        ];

        this.rowSort();

        this.data = new Map();
        for (let d of this.fulldata) {
            this.data.set(d['chainid'], d);
        }

        this.dataloading = false;

        if (this.tabformat) {
            this.onTabSelect();
        }
        this.onexport = false;
    }

    rowSort() {
        switch (this.rowsortmode) {
            case 0:
                this.rowdata = this.rowdata.sort(function(a, b) {
                    if (a['star'] == b['star']) {
                        return a['pinyin'].localeCompare(b['pinyin']);
                    }
                    if (a['star']) { return -1; }
                    return 1;
                })
                break;
            case 1:
                this.rowdata = this.rowdata.sort((a, b) => (a['pinyin'].localeCompare(b['pinyin'])))
                break;
            case 2:
                this.rowdata = this.rowdata.sort(function(a, b) {
                    if (a['zone'] == b['zone']) {
                        return a['pinyin'].localeCompare(b['pinyin']);
                    }
                    if (a['zone'] == 1) { return -1; }
                    return 1;
                })
                break;
            case 3:
                this.rowdata = this.rowdata.sort(function(a, b) {
                    if (a['zone'] == b['zone']) {
                        if (a['star'] == b['star']) {
                            return a['pinyin'].localeCompare(b['pinyin']);
                        }
                        if (a['star']) { return -1; }
                        return 1;
                    }
                    if (a['zone'] == 1) { return -1; }
                    return 1;
                })
                break;
        }
    }

    layout() {

        if (this._summaryOK == false) {
            this.summary();
            this._summaryOK = true;
        }

        this.z_st_h = this.canvasHeight - this.z_r_h - this.z_q_h;
        this.stdEm = this.z_st_h / (this.rowdata.length + 3.6);
        this.z_t_h = Math.round(this.stdEm * 3.6);
        this.z_s_h = this.z_st_h - this.z_t_h;

        this.i_s_h = this.z_s_h / this.rowdata.length;

        for (let col of this.coldata) {
            if (col.type == 'symbols') {
                col['width'] = (col.pw + 1) * this.stdEm;
            }
        }

        this.z_C_w = this.canvasWidth - this.z_A_w - this.z_B_w;

        this.rows = [];
        if (this.tabformat) {
            this.rows.push(['q', '', 0, 1, 0, this.z_q_h]);
        }
        this.rows.push(['r', '', 0, 1, this.z_q_h, this.z_r_h]);

        var i = 0;
        for (let [y, h] of divideByInteger(this.z_s_h, this.rowdata.length)) {
            this.rows.push(['s', this.rowdata[i], i, this.rowdata.length, this.z_q_h + this.z_r_h + y, h]);
            i += 1;
        }

        i = 0;
        var t_row_names = ['总计', '中影', '累计'];
        for (let [y, h] of divideByInteger(this.z_t_h, t_row_names.length)) {
            this.rows.push(['t', t_row_names[i], i, t_row_names.length, this.z_q_h + this.z_r_h + this.z_s_h + y, h]);
            i += 1;
        }

        this.cols = [];
        var x = 0;
        this.cols.push(['A', '', 0, 1, 0, this.z_A_w]);
        x += this.z_A_w;
        this.cols.push(['B', '', 0, 1, x, this.z_B_w]);
        x += this.z_B_w;

        var idx = 0;
        var colweights = this.coldata.map(c => c['width']);
        for (let [xi, w] of divideByWeight(this.z_C_w, colweights)) {
            this.cols.push(['C', this.coldata[idx], idx, this.coldata.length, x + xi, w]);
            idx += 1;
        }

    }


    summary() {

        var ctx = this.can.getContext('2d');

        this.totaldata = {};
        this.diffdata = {}
        this.col_totalw = 0;


        for (let col of this.coldata) {

            ctx.font = this.z_stC_font;

            var k = col['key'];
            var w = parseInt(col['w']);
            var t = null;
            var d = null;
            var opts = [];

            switch (col.type) {

                case 'str':

                    w = this.fulldata.reduce((a, b) => Math.max(a, ctx.measureText(b[k]).width), 0);

                    if (this.zhongdata[k] || this.zhongdata[k] === 0) {
                        w = Math.max(w, ctx.measureText(this.zhongdata[k]).width);
                    }

                    opts = Array.from(new Set(this.fulldata.map(a => a[k]))).sort();
                    t = opts.length;

                    break;

                case 'int':

                    var pds = this.fulldata.reduce((a, b) => a + Math.max(b[k], 0), 0);
                    var nds = this.fulldata.reduce((a, b) => a + Math.min(b[k], 0), 0);
                    w = Math.max(ctx.measureText('' + pds).width, ctx.measureText('' + nds).width);

                    t = this.fulldata.reduce((a, b) => parseFloat(a) + parseFloat(b[k]), 0);

                    if (this.zhongdata[k] || this.zhongdata[k] === 0) {
                        w = Math.max(w, ctx.measureText(this.zhongdata[k]).width);
                        d = -(-t - this.zhongdata[k]); // 差异改累计
                    }

                    break;

                case 'money':

                    var pds = this.fulldata.reduce((a, b) => a + Math.max(b[k], 0), 0);
                    var nds = this.fulldata.reduce((a, b) => a + Math.min(b[k], 0), 0);
                    pds = (pds / 100).toFixed(2).replace(this.money_re, "$1,");
                    nds = (nds / 100).toFixed(2).replace(this.money_re, "$1,");
                    w = Math.max(ctx.measureText(pds).width, ctx.measureText(nds).width);

                    t = this.fulldata.reduce((a, b) => parseFloat(a) + parseFloat(b[k]), 0);

                    if (this.zhongdata[k] || this.zhongdata[k] === 0) {
                        var zds = (this.zhongdata[k] / 100).toFixed(2).replace(this.money_re, "$1,");
                        w = Math.max(w, ctx.measureText(zds).width);
                        d = t - (-this.zhongdata[k]); // 差异改累计
                    }

                    break;

                case 'symbols':

                    let s_ch_format = [];
                    let s_zy_format = [];

                    if (this.colformat['chain_' + col['key']]) {
                        s_ch_format = this.colformat['chain_' + col['key']];
                    } else if (this.colformat['chain']) {
                        s_ch_format = this.colformat['chain'];
                    }

                    if (this.colformat['zhongying_' + col['key']]) {
                        s_zy_format = this.colformat['zhongying_' + col['key']];
                    } else if (this.colformat['zhongying']) {
                        s_zy_format = this.colformat['zhongying'];
                    }

                    col['format'] = {
                        'chain': s_ch_format,
                        'zhongying': s_zy_format,
                    }

                    col['pw'] = Math.max(s_ch_format.length, s_zy_format.length);

                    w = 0;
                    break;
            }

            ctx.font = this.z_rC_font;
            w = col['display'].split('\n').reduce((a, b) => Math.max(a, ctx.measureText(b).width), w);

            col['width'] = parseInt(w) + 20;
            this.totaldata[k] = t;
            this.diffdata[k] = d;

            this.col_totalw += col['width'];

        }

    }


    draw(deep) {

        var ctx = this.can.getContext('2d');

        for (let [ct, cv, ci, cm, cx, cw] of this.cols) {

            if (ct == 'A') {
                ctx.fillStyle = "#FAFAFA";
                ctx.fillRect(cx, this.z_q_h, cw, this.canvasHeight);
                ctx.fillStyle = "#F6F6F6";
                ctx.fillRect(cx, this.z_q_h, cw, this.canvasHeight - this.z_t_h);
            }

            if (ct == 'B') {
                ctx.fillStyle = "#FAFAFA";
                ctx.fillRect(cx, this.z_q_h, cw, this.canvasHeight);
            }

            if (ct == 'C') {

                if (cv['red']) {
                    ctx.fillStyle = "#FFFAFA";
                    ctx.fillRect(cx, this.z_q_h, cw, this.canvasHeight);
                }

            }

            if (this.select && ct == this.select[0] && ci == this.select[1]) {
                ctx.fillStyle = "#f0f9ff";
                ctx.fillRect(cx, this.z_q_h, cw, this.canvasHeight);
            }
        }

        for (let [rt, rv, ri, rm, ry, rh] of this.rows) {

            if (this.select && rt == this.select[4] && ri == this.select[5]) {
                ctx.fillStyle = "#d2eeff";
                ctx.fillRect(this.z_A_w + this.z_B_w, ry, this.canvasWidth, rh);
            }

            if (rt == 'q') {
                ctx.fillStyle = "#EEE";
                ctx.fillRect(0, ry, this.canvasWidth, rh);

                this.tabsprites = [];
                let tabn = Math.round(this.canvasWidth / 110);
                let stepw = parseInt((this.canvasWidth - (tabn + 1) * 5 - 50) / tabn);
                let xx = this.canvasWidth - stepw - 5;
                let datedelta = 0;

                for (; datedelta < tabn; xx -= stepw + 5, datedelta++) {

                    let dm = new Date(this.firstday);
                    dm.setMonth(dm.getMonth() - datedelta);

                    if (datedelta + 1 == tabn && this.today.getYear() * 100 + this.today.getMonth() < dm.getYear() * 100 + dm.getMonth()) {
                        dm = new Date(this.today);
                    }

                    this.tabsprites.push({ 'x': xx, 'w': stepw, 'date': dm, 'dropdown': (datedelta + 1 == tabn) });

                    if (('' + dm) == ('' + this.today)) {

                        ctx.shadowOffsetX = 2;
                        ctx.shadowOffsetY = 0;
                        ctx.shadowBlur = 4;
                        ctx.shadowColor = "rgba(0, 0, 0, 0.1)"; //or use rgb(red, green, blue)

                        ctx.fillStyle = "#FAFAFA";
                        ctx.fillRect(0, ry + rh, this.canvasWidth, this.z_r_h / 2);
                        ctx.fillRect(xx, ry + 3, stepw, rh - 3);

                        ctx.shadowOffsetX = 0;
                        ctx.shadowOffsetY = 0;
                        ctx.shadowBlur = 0;
                        ctx.shadowColor = null;

                    } else {

                        ctx.beginPath();
                        ctx.strokeStyle = "#CCC";
                        ctx.moveTo(xx + 0.5, ry + 10);
                        ctx.lineTo(xx + 0.5, ry + rh - 9);
                        ctx.stroke();

                    }

                    ctx.font = '10px 微软雅黑';
                    ctx.textBaseline = 'middle';
                    ctx.fillStyle = "#555";
                    ctx.textAlign = 'left';

                    let strdate = '' + dm.getFullYear() + '-';
                    strdate += ('' + (dm.getMonth() + 1)).padStart(2, '0');
                    let sym = this.tabformat[this.datetab[strdate]];
                    if (sym) {
                        draw_symbol(ctx, sym, xx + 15, ry + rh / 2, this.stdEm, 1, 0);
                    }
                    ctx.fillText(strdate, xx + 27, ry + rh / 2);

                    if (datedelta + 1 == tabn) {

                        ctx.font = '16px FontAwesome';
                        ctx.textBaseline = 'middle';
                        ctx.fillStyle = "#555";
                        ctx.textAlign = 'right';
                        ctx.fillText('\uf103', xx + stepw - 8, ry + rh / 2);
                    }

                }

                xx = this.canvasWidth - (stepw + 5) * tabn;

                ctx.font = '14px FontAwesome';
                ctx.textBaseline = 'middle';
                ctx.fillStyle = "#555";
                ctx.textAlign = 'center';
                ctx.fillText('\uf0db', xx / 2, ry + rh / 2); //'\uf073'

                this.tabsprites.push({ 'x': 5, 'w': xx - 5, 'date': null, 'dropdown': false, 'calendar': true });
            }

            if (rt == 'r') {
                ctx.fillStyle = "#FAFAFA";
                ctx.fillRect(0, ry, this.canvasWidth, rh);

                ctx.beginPath();
                ctx.strokeStyle = "#CCC";
                ctx.moveTo(0, ry + rh - 0.5);
                ctx.lineTo(this.canvasWidth, ry + rh - 0.5);
                ctx.stroke();

            }

            if (rt == 't') {
                ctx.fillStyle = "#EEE";
                ctx.globalAlpha = 0.2;
                ctx.fillRect(0, ry, this.canvasWidth, rh);
                ctx.fillStyle = "#FAFAFA";
                ctx.globalAlpha = 1;
                ctx.beginPath();
                ctx.strokeStyle = "#CCC";
                ctx.moveTo(0, ry + 0.5);
                ctx.lineTo(this.canvasWidth, ry + 0.5);
                ctx.stroke();
            }

            if (rt == 's' && ri + 1 != rm) {
                ctx.beginPath();
                ctx.strokeStyle = "#E4E4E4";
                ctx.moveTo(0, ry + rh - 0.5);
                ctx.lineTo(this.z_A_w + this.z_B_w, ry + rh - 0.5);
                ctx.stroke();
                ctx.beginPath();
                ctx.strokeStyle = "#F0F0F0";
                if (this.select && rt == this.select[4] && (ri == this.select[5] || ri == this.select[5] - 1)) {
                    ctx.strokeStyle = "#50bdff";
                }
                ctx.moveTo(this.z_A_w + this.z_B_w, ry + rh - 0.5);
                ctx.lineTo(this.canvasWidth, ry + rh - 0.5);
                ctx.stroke();
            }

            ctx.font = '12px 微软雅黑';
            ctx.textBaseline = 'middle';
            ctx.fillStyle = "#555";
            ctx.textAlign = 'right';

            if (rt == 's') {
                ctx.fillText(rv['chain'], this.z_A_w + this.z_B_w - 5, ry + rh / 2);
            }

            if (rt == 't') {
                ctx.fillText(rv, this.z_A_w + this.z_B_w - 5, ry + rh / 2);
            }

            ctx.font = '9px 微软雅黑';
            ctx.textBaseline = 'middle';
            ctx.fillStyle = "#555";
            ctx.textAlign = 'left';

            if (rt == 's') {
                ctx.fillText('-甲乙' [rv['zone']], 8, ry + rh / 2);
            }

            if (rt == 's' && rv['star']) {
                ctx.fillStyle = "#FF9F9F";
                ctx.fillRect(0, ry, 3, rh);
            }


        }

        for (let [ct, cv, ci, cm, cx, cw] of this.cols) {

            if (ct == 'B') {
                ctx.font = '12px FontAwesome';
                ctx.textBaseline = 'middle';
                ctx.fillStyle = "#444";
                ctx.textAlign = 'right';

                ctx.fillText(this.rowsortmodenames[this.rowsortmode], cx + cw - 10, this.z_q_h + this.z_r_h - 10);
            }

            if (ct != 'A' && !(ct == 'D' && ci == cm - 1)) {

                ctx.beginPath();
                ctx.strokeStyle = (ci == cm - 1) ? "#BBB" : "#DDD";
                ctx.moveTo(cx + cw - 0.5, this.z_q_h);
                ctx.lineTo(cx + cw - 0.5, this.z_q_h + this.z_r_h);
                ctx.stroke();

                ctx.beginPath();
                ctx.strokeStyle = (ci == cm - 1) ? "#DDD" : "#F0F0F0";
                if (ct == 'C' && cv['line']) {
                    ctx.strokeStyle = cv['line'];
                }
                if (this.select && ct == this.select[0] && (ci == this.select[1] || ci == this.select[1] - 1)) {
                    ctx.strokeStyle = "#50bdff";
                }
                ctx.moveTo(cx + cw - 0.5, this.z_q_h + this.z_r_h);
                ctx.lineTo(cx + cw - 0.5, this.canvasHeight);
                ctx.stroke();

            }

            if (ct == 'C') {

                var tx;
                var ty;

                ctx.font = this.z_rB_font;

                ctx.textAlign = cv['align']

                switch (cv['align']) {
                    case 'center':
                        tx = cx + cw / 2;
                        break;
                    case 'left':
                        tx = cx + 10;
                        break;
                    case 'right':
                        tx = cx + cw - 10;
                        break;
                }

                var t_n = 0;
                var t_lns = cv['display'].split('\n');
                for (let t_ln of t_lns) {
                    ty = this.z_q_h + this.z_r_h - 5 - 18 * (t_lns.length - 0.5 - t_n);
                    ctx.fillText(t_ln, tx, ty);
                    t_n += 1;
                }

            }

        }

        this.draw_data(ctx);

        ctx.save();
        ctx.translate(3, this.canvasHeight - 3);

        ctx.fillStyle = '#666';
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(13, 0);
        ctx.lineTo(0, -13);
        ctx.closePath()
        ctx.fill();

        ctx.fillStyle = '#aaa';
        ctx.font = '11px 微软雅黑';
        ctx.textAlign = 'left';
        ctx.textBaseline = 'bottom';
        ctx.fillText(this.onexport ? '保存中' : '导出', 14, 2);

        ctx.restore();

    }

    draw_data(ctx) {

        if (this.dataloading) {
            var pattern = ctx.createPattern(this.loadpattern, "repeat");
            ctx.fillStyle = pattern;
            let y = this.z_q_h + this.z_r_h;
            let x = this.z_A_w + this.z_B_w;
            ctx.fillRect(x, y, this.canvasWidth, this.canvasHeight);
            return;
        }

        for (let [rt, rv, ri, rm, ry, rh] of this.rows) {

            if (rt == 's') {

                var d = this.data.get(rv['chainid']);

                var ty = ry + rh / 2;
                var tx;
                var t;

                var ct, cv, ci, cm, cx, cw;

                for (let [ct, cv, ci, cm, cx, cw] of this.cols) {
                    let d_cv_key = d && cv ? d[cv['key']] : 0;
                    if (ct == 'C') {

                        if (cv['type'] == 'symbols') {

                            let cdata = d_cv_key;
                            if (!cdata) { cdata = {} }

                            let ii = 0;
                            let fmt = cv['format']['chain'];
                            for (let ifmt of fmt) {
                                let ix = cx + (cw * (ii + 1)) / (fmt.length + 1);
                                let iy = (rt == 'r') ? (ry + rh - this.stdEm) : (ry + rh / 2);
                                let showtype = ifmt['show'];
                                let idata = cdata[ifmt['key']];
                                let idata_badge = cdata[ifmt['key'] + '-badge'];
                                idata_badge = idata_badge ? idata_badge : '';

                                if (idata) {

                                    draw_symbol(ctx, showtype, ix, iy, this.stdEm, idata, idata_badge);

                                } else {

                                    ctx.save();
                                    ctx.translate(ix, iy);

                                    ctx.fillStyle = 'rgba(0,0,0,0.06)';
                                    ctx.beginPath();
                                    ctx.arc(0, 0, 2, 0, 2 * Math.PI);
                                    ctx.fill();

                                    ctx.restore();
                                }

                                ii += 1
                            }

                            continue;
                        }

                        ctx.font = this.z_stC_font;

                        ctx.textAlign = cv['align'];

                        switch (cv['align']) {
                            case 'center':
                                tx = cx + cw / 2;
                                break;
                            case 'left':
                                tx = cx + 10;
                                break;
                            case 'right':
                                tx = cx + cw - 10;
                                break;
                        }

                        if (cv['type'] == 'money') {
                            if (d === undefined || d_cv_key === undefined) {
                                t = '';
                            } else {
                                t = (d_cv_key / 100).toFixed(2);
                                t = t.replace(this.money_re, "$1,");
                            }
                        } else {
                            t = '' + (d && cv ? d_cv_key : "");
                        }
                        if (cv['watch']) { // 系数是str
                            const a = cv['watch'];
                            let b = 0;
                            if (cv['type'] == 'money') {
                                b = (d_cv_key / 100).toFixed(2)
                            } else {
                                b = d_cv_key
                            }
                            if (!isNaN(b) && a(b)) {
                                ctx.save();
                                ctx.fillStyle = "#FFCCCC";
                                ctx.fillRect(cx, ry, cw - 1, rh - 1);
                                ctx.restore();
                            }
                        } else if (['money', 'int'].includes(cv['type']) && d !== undefined && d_cv_key < 0) {
                            ctx.save();
                            ctx.fillStyle = "#FFCCCC";
                            ctx.fillRect(cx, ry, cw - 1, rh - 1);
                            ctx.restore();
                        }
                        // if (['money', 'int'].includes(cv['type']) && d[cv['key']] < 0) {
                        //     ctx.save();
                        //     ctx.fillStyle = "#FFCCCC";
                        //     ctx.fillRect(cx, ry, cw - 1, rh - 1);
                        //     ctx.restore();
                        // }

                        ctx.fillText(t, tx, ty);

                    }

                }
            }

            if (rt == 't') {

                var ty = ry + rh / 2;
                var tx;
                var t;

                var d = [this.totaldata, this.zhongdata, this.diffdata][ri]

                for (let [ct, cv, ci, cm, cx, cw] of this.cols) {

                    if (ct != 'C') { continue; }

                    if (cv['type'] == 'symbols') {

                        let cdata = d[cv['key']];
                        if (!cdata) { cdata = null; }

                        if (cdata) {

                            let ii = 0;
                            let fmt = cv['format']['zhongying'];
                            for (let ifmt of fmt) {
                                let ix = cx + (cw * (ii + 1)) / (fmt.length + 1);
                                let iy = (rt == 'r') ? (ry + rh - this.stdEm) : (ry + rh / 2);
                                let showtype = ifmt['show'];
                                let idata = cdata[ifmt['key']];
                                let idata_badge = cdata[ifmt['key'] + '-badge'];
                                idata_badge = idata_badge ? idata_badge : '';

                                if (idata) {

                                    draw_symbol(ctx, showtype, ix, iy, this.stdEm, idata, idata_badge);

                                } else {

                                    ctx.save();
                                    ctx.translate(ix, iy);

                                    ctx.fillStyle = 'rgba(0,0,0,0.06)';
                                    ctx.beginPath();
                                    ctx.arc(0, 0, 2, 0, 2 * Math.PI);
                                    ctx.fill();

                                    ctx.restore();
                                }

                                ii += 1;
                            }

                        }

                        continue;
                    }

                    //var d = this.totaldata;
                    ctx.font = this.z_stC_font;

                    ctx.textAlign = cv['align'];

                    switch (cv['align']) {
                        case 'center':
                            tx = cx + cw / 2;
                            break;
                        case 'left':
                            tx = cx + 10;
                            break;
                        case 'right':
                            tx = cx + cw - 10;
                            break;
                    }

                    if (cv['type'] == 'money') {
                        t = (d[cv['key']] / 100).toFixed(2)
                        t = t.replace(this.money_re, "$1,")
                    } else {
                        t = '' + d[cv['key']]
                    }

                    if (['money', 'int'].includes(cv['type']) && d[cv['key']] < 0) {
                        ctx.fillStyle = '#FF4466';
                    } else {
                        ctx.fillStyle = '#555';
                    }

                    ctx.fillText(t, tx, ty);
                }

            }
        }
    }

    onClick_stCD(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.select = [ct, ci, cx, cw, rt, ri, ry, rh];
        let cdata = this.data.get(rv['chainid']);
        // 复制点击的内容
        let copyValue = '';
        if (cdata) {
            copyValue = cdata[cv.key];
        } else if (rv === '总计') {
            copyValue = this.totaldata[cv['key']];
        } else if (rv === '中影') {
            copyValue = this.zhongdata[cv['key']];
        } else if (rv === '累计') {
            copyValue = this.diffdata[cv['key']];
        }

        if (copyValue) {
            if (cv.type === 'money') {
                copyValue = (copyValue / 100).toFixed(2);
            }
            const aux = document.createElement('input');
            aux.setAttribute('value', copyValue);
            document.body.appendChild(aux);
            aux.select();
            document.execCommand('copy');
            document.body.removeChild(aux);
        }
        if (rt == 's' && cdata) {
            cdata = cdata[rv['chainid']];
        }
        let args = {
            'col': cv,
            'row': rv,
            'data': cdata,
        }

        let onselect = this.getAttribute('onselect');

        if (onselect) {
            safePromiseEval(onselect, args);
        }

        this.redraw();

        return;
    }

    onClick_tAB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.cancel_select();
        console.log(x, y);
        if (y < this.canvasHeight - 30 && x < 60) return;
        // if (y < this.canvasHeight - 30) return; // rh/3
        if (this.onexport) return;

        if (!this.data.size) {
            console.log('无数据，不导出！');
            this.exportEnd();
            return;
        };

        this.onexport = true;
        this.redraw();
        let opt = { 'filters': [{ 'name': 'CSV FILE', 'exts': '*.csv' }], 'filename': (window.exportFileName ? window.exportFileName : 'export.csv') };
        eui.saveFile(opt).then(resolve => this.exportFile(resolve), reject => this.exportEnd());
    }

    exportFile(fn) {
        var exportdata = [];
        var coldata = JSON.parse(JSON.stringify(this.coldata));
        var dataMap = new Map;
        this.data.forEach((key, obj) => {
            dataMap.set(key, JSON.parse(JSON.stringify(obj)));
        });

        var total = JSON.parse(JSON.stringify(this.totaldata));
        var exportd = JSON.parse(JSON.stringify(this.zhongdata));
        var diff = JSON.parse(JSON.stringify(this.diffdata));

        coldata.unshift({
            align: 'left',
            key: 'zonename',
            display: '分区',
            type: 'str',
            w: 50,
            width: 50
        });
        coldata.unshift({
            align: 'left',
            key: 'chainname',
            display: '院线',
            type: 'str',
            w: 50,
            width: 50
        });
        for (let irow of this.rows) {
            if (typeof irow[1] === 'object') {
                let rowObj = this.data.get(irow[1]['chainid']);
                rowObj.chainname = irow[1]['chain'];
                rowObj.zonename = irow[1]['zone'] === 1 ? '甲区' : '乙区';
                exportdata.push(rowObj);
            } else if (irow[1] === '总计') {
                total.chainname = irow[1];
                total.zonename = '';
                exportdata.push(total);
            } else if (irow[1] === '中影') {
                exportd.chainname = irow[1];
                exportd.zonename = '';
                exportdata.push(exportd);
            } else if (irow[1] === '累计') {
                diff.chainname = irow[1];
                diff.zonename = '';
                for (let d in diff) {
                    if (diff[d] === null) {
                        diff[d] = '0';
                    }
                }
                exportdata.push(diff);
            }
        }
        eui.exportSheet(fn, coldata, exportdata).then(resolve => this.exportEnd());
    }

    exportEnd() {
        this.onexport = false;
        this.redraw();
    }

    onClick_sC(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.onClick_stCD(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y);
    }

    onClick_sD(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.onClick_stCD(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y);
    }

    onClick_tC(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.onClick_stCD(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y);
    }

    onClick_tD(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.onClick_stCD(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y);
    }

    onClick_tA(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.onClick_tAB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y);
    }

    onClick_tB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.onClick_tAB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y);
    }

    cancel_select() {

        this.select = null;

        let args = {
            'col': null,
            'row': null,
            'data': null,
        }

        let onselect = this.getAttribute('onselect');

        if (onselect) {
            safePromiseEval(onselect, args);
        }

        this.redraw();

        return;
    }

    onClick_sA(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.cancel_select();
    }

    // onClick_tA(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
    //     this.cancel_select();
    // }

    onClick_sB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.cancel_select();
    }

    // onClick_tB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
    //     this.cancel_select();
    // }

    onClick_rC(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.cancel_select();
    }

    onClick_rB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.rowsortmode = (this.rowsortmode + 1) % 4;
        this.rowSort();
        this.layout();
        this.cancel_select();
    }

    onDblClick_sA(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        rv['star'] = rv['star'] ? false : true;

        let args = {
            'row': rv,
        }

        let onsetstar = this.getAttribute('onsetstar');

        if (onsetstar) {
            safePromiseEval(onsetstar, args);
        }

        this.rowSort();
        this.layout();
        this.cancel_select();
    }

    onClick_qA(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.onClick_q(x, y);
    }

    onClick_qB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.onClick_q(x, y);
    }

    onClick_qC(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {
        this.onClick_q(x, y);
    }

    onClick_q(x, y) {
        for (let ts of this.tabsprites) {
            if (x > ts.x && x < ts.x + ts.w) {

                if (ts.calendar) {

                    let onselect = this.getAttribute('oncalendar');
                    if (onselect) {
                        safePromiseEval(onselect, {});
                    }

                    return;

                }

                if (ts.dropdown) {

                    this.dropdown.style['display'] = 'block';
                    this.shaddow.style['display'] = 'block';
                    this.dropdown.querySelector('.rdg_year').value = '' + ts.date.getFullYear();
                    // this.dropdown.querySelector('.rdg_month').value = '' + (ts.date.getMonth() + 1);

                    return;
                }

                this.today = new Date(ts.date);

                this.clearData();

                return;
            }
        }

    }

    reload_data(ks, rs) {

        var args = {};
        for (let i = 0; i < ks.length; i++) {
            args[ks[i]] = rs[i];
        }

        this.datetab = args['datetab'];

        this.tabsprites = [];

        this.fulldata = (args['fulldata'] ? args['fulldata'] : []);
        this.zhongdata = (args['zhongdata'] ? args['zhongdata'] : {});

        this._summaryOK = false;
        this.select = null;

        this.data = new Map();
        for (let d of this.fulldata) {
            this.data.set(d['chainid'], d);
        }

        this.dataloading = false;

        this._summaryOK = false;
        this.layout();
        this.cancel_select();

    }

    onTabSelect() {

        let onselect = this.getAttribute('ontabselect');
        let strdate = '' + this.today.getFullYear() + '-';
        strdate += ('' + (this.today.getMonth() + 1)).padStart(2, '0');
        let sym = this.tabformat[this.datetab[strdate]];

        let arg = {
            'date': this.today,
            'strDate': this.today.toLocaleDateString(),
            'tab': strdate,
            'value': this.datetab[strdate],
            'symbol': sym,
        }

        if (onselect) {
            safePromiseEval(onselect, arg);
        }

        return;
    }

    clearData() {

        this.onTabSelect();

        let m = {};
        m['date'] = this.today;
        m['strDate'] = this.today.toLocaleDateString();

        let ks = [];
        let ps = [];

        ks.push('datetab');
        ps.push(safePromiseEval(this.getAttribute('datetab'), m));

        ks.push('fulldata');
        ps.push(safePromiseEval(this.getAttribute('fetchdata'), m));

        ks.push('zhongdata');
        ps.push(safePromiseEval(this.getAttribute('fetchzhongying'), m));

        Promise.all(ps).then(rs => this.reload_data(ks, rs));

        this.data = new Map();
        this.dataloading = true;
        this._summaryOK = false;
        this.layout();
        this.cancel_select();

    }
    cancel() {
        this.dropdown.style['display'] = 'none';
        this.shaddow.style['display'] = 'none';
    }
    right_year() {
        let _select = this.dropdown.children[1];
        if (_select.selectedIndex > 0) {
            _select.selectedIndex = _select.selectedIndex - 1;
        }
    }

    left_year() {
        let _select = this.dropdown.children[1];
        if (_select.selectedIndex < (_select.children.length - 1)) {
            _select.selectedIndex = _select.selectedIndex + 1;
        }
    }

    gotoDate(this_month) {
        var year = this.dropdown.querySelector('.rdg_year').value;
        var month = this_month;
        if (!this_month) {
            month = ((new Date()).getMonth()) + 1
            year = (new Date()).getFullYear()
        }

        this.dropdown.style['display'] = 'none';
        this.shaddow.style['display'] = 'none';

        year = parseInt(year);
        month = parseInt(month);
        if (!(year && month)) {
            return;
        }
        if (year > this.firstday.getFullYear() || year < 2012) {
            return;
        }
        if (month > 12 || month < 1) {
            return;
        }
        var dt = new Date(year, month - 1);
        if (dt.getFullYear() * 100 + dt.getMonth() > this.firstday.getFullYear() * 100 + this.firstday.getMonth()) {
            return;
        }
        this.today = dt;

        this.clearData();

    }

}



class CalendarGraphData extends DataGrid {

    constructor() {
        super();
        this.prepare = [
            ['period', 'period'],
            ['fulldata', 'fetchdata']
        ];
        this.flexible = false;
        this.clickable = false;
    }

    init(args) {

        this.startdate = this.parseDate(args['period'].start);
        this.enddate = this.parseDate(args['period'].end);
        this.fulldata = new Map();

        this.firstdate = this.startdate;
        this.lastdate = this.enddate;

        for (let i of args['fulldata']) {
            var d = this.parseDate(i['showdate']);
            this.fulldata[d.getTime()] = i;
            this.firstdate = Math.min(d, this.firstdate);
            this.lastdate = Math.max(d, this.lastdate);
        }

        //this.firstdate = this.fulldata.reduce((a,b)=>Math.min(a,b), this.startdate);
        //this.lastdate = this.fulldata.reduce((a,b)=>Math.max(a,b), this.enddate);

        this.blocksize = 10;
        this.blockgap = 2;
        this.border = 10;

    }

    parseDate(d) {
        if (typeof d == 'string') {
            let [yy, mm, dd] = d.split('-');
            return new Date(parseInt(yy), parseInt(mm) - 1, parseInt(dd), 0, 0, 0);
        }
        d.setHours(0);
        d.setMinutes(0);
        d.setSeconds(0);
        d.setMilliseconds(0);
        return d;
    }

    isoweekfirstday(d) {
        var isoweekday = (6 + d.getDay()) % 7;
        d.setDate(d.getDate() - isoweekday);
    }

    layout() {

        this.firstweek = new Date(this.firstdate.getTime());
        this.lastweek = new Date(this.lastdate.getTime());

        //console.log(this.startdate.toISOString(), this.enddate.toISOString());

        //console.log( this.firstweek.getDay() );
        //console.log(( (6+this.firstweek.getDay()) %7));

        this.isoweekfirstday(this.firstweek.toISOString());
        this.isoweekfirstday(this.lastweek.toISOString());

        //.setDate(this.firstweek.getDate()-(6+this.firstweek.getDay()%7));
        //this.lastweek.setDate(this.lastweek.getDate()-(6+this.lastweek.getDay()%7));

        //console.log(this.firstweek, this.lastweek);

        var w = new Date(this.firstweek.getTime());

        this.cols = [];
        this.rows = [];

        //[ct, cv, ci, cm, cx, cw]

        var ln = 0;
        //var weeks = (this.lastweek - this.firstweek)/(7*24*3600*1000);
        while (w.getTime() <= this.lastdate.getTime()) {
            let cw = new Date(w.getTime());
            this.cols.push(['w', cw, ln, 0, ln * (this.blocksize + this.blockgap), this.blocksize]);
            w.setDate(w.getDate() + 7);
            ln += 1;
        }

        //var xspace = this.canvasWidth - ln*this.blocksize - (ln-1)*this.blockgap;
        //xspace = parseInt(xspace/2);
        //xspace = Math.max(xspace, 0);
        for (let c of this.cols) {
            c[3] = ln;
            c[4] = this.border + c[4];
        }

        //var yspace = this.canvasHeight - 7*this.blocksize - 6*this.blockgap;
        //yspace = parseInt(yspace/2);
        //yspace = Math.max(yspace, 0);
        var weekdaynames = ['一', '', '', '', '', '', '日']
        for (ln = 0; ln < 7; ln++) {
            this.rows.push(['d', weekdaynames[ln], ln, 7, this.border + ln * (this.blocksize + this.blockgap), this.blocksize]);
        }

        this.can.width = this.cols.length * this.blocksize + (this.cols.length - 1) * this.blockgap + this.border * 2;
        this.can.height = this.rows.length * this.blocksize + (this.rows.length - 1) * this.blockgap + this.border * 2;

    }


    draw(deep) {

        var ctx = this.can.getContext('2d');

        for (let [ct, cv, ci, cm, cx, cw] of this.cols) {

            for (let [rt, rv, ri, rm, ry, rh] of this.rows) {

                let w = new Date(cv.getTime());
                w.setDate(w.getDate() + ri);

                if (w < this.startdate || w > this.enddate) {
                    ctx.strokeStyle = "#e9e9e9";
                    ctx.strokeRect(cx, ry, cw, rh);
                } else {
                    ctx.fillStyle = "#e9e9e9";
                    ctx.fillRect(cx, ry, cw, rh);
                }

            }

        }
    }

}


class MovieTrackBlock extends Sprite {

    constructor(parent, data, hallidx = null, startMark = null) {

        super(parent, 0, 0, 0, 0, true);

        let keys = [
            'start_time',
            'end_time',
            'duration',
            'created_at',
            'screen_code',
            'film_name',
            'film_code',
            'image',
            'language',
            'price_plan_id',
            'price_plan',
            'share_proportion',
        ];

        this.data = {};
        for (let k in data) {
            if (keys.includes(k)) {
                this.data[k] = data[k];
            }
        }

        this.hallidx = hallidx;

        if (this.hallidx == null) {
            this.hallidx = this.parent.code2hallidx[this.data.screen_code];
        }

        this.durationMark = parseInt(this.data.duration / (5 * 60));
        this.durationMinutes = this.durationMark * 5;

        let startmk;
        this.startMark = startmk = startMark;
        if (this.startMark == null) {
            //let delta = parseInt(this.date.start_time) - parseInt(this.parent.bussiness_date.getTime()/1000);
            startmk = parseInt(this.data.start_time) - this.parent.bussiness_startTime;
            startmk = parseInt(startmk / (60 * 5));
            this.startMark = Math.max(startmk, 0);
            this.startIn = (this.startMark == startmk) ? true : false;
        } else {
            this.startIn = true;
        }

        this.endMark = Math.min((startmk + this.durationMark), 28 * 12);
        this.endIn = (this.endMark == (startmk + this.durationMark)) ? true : false;


    }

    dump() {

        this.data.start_time = this.parent.bussiness_startTime + this.startMark * 5 * 60;
        this.data.end_time = this.parent.bussiness_startTime + this.endMark * 5 * 60;

        let start_m = this.startMark * 5;
        let start_h = parseInt(start_m / 60) + 6;

        start_m = parseInt(start_m % 60);

        let end_m = this.endMark * 5;
        let end_h = parseInt(end_m / 60) + 6;

        end_m = parseInt(end_m % 60);

        // this.data.b30h_start_time = (''+start_h).padStart(2,'0')+':'+(''+start_m).padStart(2,'0');
        // if ( end_h < 30 ){
        //   this.data.b30h_end_time = (''+end_h).padStart(2,'0')+':'+(''+end_m).padStart(2,'0');
        // } else {
        //   this.data.b30h_end_time = (''+(end_h-24)).padStart(2,'0')+':'+(''+end_m).padStart(2,'0')+'+1';
        // }

        if (start_h < 24) {
            this.data.b24h_start_time = ('' + start_h).padStart(2, '0') + ':' + ('' + start_m).padStart(2, '0');
        } else {
            this.data.b24h_start_time = ('' + (start_h - 24)).padStart(2, '0') + ':' + ('' + start_m).padStart(2, '0') + '+1';
        }

        if (end_h < 24) {
            this.data.b24h_end_time = ('' + end_h).padStart(2, '0') + ':' + ('' + end_m).padStart(2, '0');
        } else {
            this.data.b24h_end_time = ('' + (end_h - 24)).padStart(2, '0') + ':' + ('' + end_m).padStart(2, '0') + '+1';
        }

        this.data.screen_code = this.parent.halls[this.hallidx].code;

        if (!this.data.created_at) {
            let ct = new Date();
            this.data.created_at = ("" + ct.getFullYear()) + '-' +
                ("" + (ct.getMonth() + 1)).padStart(2, '0') + '-' +
                ("" + ct.getDate()).padStart(2, '0') + ' ' +
                ("" + ct.getHours()).padStart(2, '0') + ':' +
                ("" + ct.getMinutes()).padStart(2, '0') + ':' +
                ("" + ct.getSeconds()).padStart(2, '0');
        }

        return this.data;
    }

    onLayout() {

        var startcoord = this.parent.markCoord[this.startMark];
        var endcoord = this.parent.markCoord[this.endMark];

        var hall = this.parent.halls[this.hallidx];

        var x4 = startcoord.x;
        var x6 = endcoord.x;
        var y8 = hall.y + 5;
        var h = hall.h - 12;

        this.startTime = this.startIn ? startcoord.time : '';
        this.endTime = this.endIn ? endcoord.time : '';

        this.setPosSize(x4, y8, x6 - x4, h);

    }

    dragStart(x, y) {

        super.dragStart(x, y);
        this.init_startMark = this.startMark;
        this.init_endMark = this.endMark;

        this.parent.redraw(1);
    }

    dragEnd(x, y) {

        super.dragEnd(x, y);

        [x, y] = this.parent.mouseToCanvasPostion(x, y);

        let curx;

        curx = this.sx + x - this.mousex;
        curx = Math.max(this.parent.markCoord[0].x, curx);
        curx = Math.min(this.parent.markCoord[24 * 12 - 1].x, curx);

        this.startMark = this.parent.x2mark[curx];
        this.endMark = this.startMark + this.durationMark;

        this.onLayout();

        if (this.parent.hitTestMovieTrack(this)) {

            this.startMark = this.init_startMark;
            this.endMark = this.startMark + this.durationMark;
            //delete this.init_startMark;

            this.onLayout();
        }

        this.parent.redraw(1);

    }


    dragMove(x, y) {

        [x, y] = this.parent.mouseToCanvasPostion(x, y);

        let curx;

        curx = this.sx + x - this.mousex;
        curx = Math.max(this.parent.markCoord[0].x, curx);
        curx = Math.min(this.parent.markCoord[24 * 12 - 1].x, curx);

        var startMark = this.parent.x2mark[curx];

        if (this.startMark != startMark) {

            this.startMark = startMark;
            this.endMark = startMark + this.durationMark;

            this.onLayout();

            this.parent.redraw(1);
        }

    }

}


class TimelineTrack extends DataGrid {

    constructor() {
        super();
        this.prepare = [
            ['halls', 'halls'],
            ['bussiness_date', 'bussiness_date'],
        ];

        this.prepare2 = [
            ['programs', 'programs'],
            ['fixprograms', 'fixprograms']
        ];
        this.flexible = true;
        this.clickable = true;
        this.watchcursor = true;
        this.cursor_mode = "std";
    }

    static get observedAttributes() { return ['newprogram']; }

    attributeChangedCallback(attr, oldValue, newValue) {

        if (attr == 'newprogram') {
            try {
                this.new_program = JSON.parse(newValue);
                if (!this.new_program.film_code) {
                    this.new_program = null;
                } else if (!this.new_program.film_name) {
                    this.new_program = null;
                } else if (!this.new_program.duration) {
                    this.new_program = null;
                } else if (parseInt(this.new_program.duration) <= 0) {
                    this.new_program = null;
                } else if (!this.new_program.language) {
                    this.new_program = null;
                } else if (!this.new_program.image) {
                    this.new_program = null;
                }
            } catch (e) {
                this.new_program = null;
            }
        }

        this.redraw(1);
    }

    prepare_args(m) {
        let hallcodes = [];
        for (let hall of m['halls']) {
            hallcodes.push(hall['code']);
        }
        m['hallcodes'] = hallcodes;
    }

    dump() {
        let r = [];
        for (let s of this.sprites) {
            r.push(s.dump());
        }
        return r;
    }

    init(args) {

        this.initialTime = 6;
        this.addedTime = 4;

        this.borderLeft = 80;
        this.borderRight = 20;

        this.maxHallHeight = 80;
        this.halls = args['halls'];

        this.bussiness_date = new Date(args['bussiness_date']);
        this.bussiness_date.setHours(6);
        this.bussiness_date.setMinutes(0);
        this.bussiness_date.setSeconds(0);
        this.bussiness_date.setMilliseconds(0);

        this.bussiness_startTime = parseInt(this.bussiness_date.getTime() / 1000);

        let idx = 0;
        this.code2hallidx = {};
        for (let hall of halls) {
            this.code2hallidx[hall['code']] = idx;
            idx += 1;
        }

        this.z_r_h = 45;
        this.z_A_w = this.borderLeft;

        for (let hall_programs of args['programs']) {
            for (let programs of hall_programs['layout_films']) {
                this.sprites.push(new MovieTrackBlock(this, programs));
            }
        }

        this.fixsprites = [];

        for (let type_programs in args['fixprograms']) {
            for (let hall_programs of args['fixprograms'][type_programs]) {
                for (let programs of hall_programs['layout_films']) {
                    this.fixsprites.push(new MovieTrackBlock(this, programs));
                }
            }
        }

        this.innerHTML = `
    <canvas></canvas>
    <canvas></canvas>
    <canvas></canvas>
    <canvas></canvas>
    `
    }

    layout() {

        this.markCoord = [];
        this.x2mark = {};

        var timelineWidth = this.canvasWidth - this.borderLeft - this.borderRight;

        this.cols = [];
        this.rows = [];

        let idx = 0;
        for (let [x, w] of divideByInteger(timelineWidth, (24 + this.addedTime) * 12)) {

            let hh = (parseInt(idx / 12) + this.initialTime) % 24;
            let mm = parseInt(idx % 12) * 5;

            let tmstr = ('' + hh).padStart(2, '0') + ':' + ('' + mm).padStart(2, '0');
            this.markCoord.push({ 'x': this.z_A_w + x, 'time': tmstr, 'idx': idx, 'w': w, 'hour': hh, 'minutes': mm, 'today': (idx < 24 * 12) });

            for (let xx = 0; xx < w; xx++) {
                this.x2mark[this.z_A_w + x + xx] = idx;
            }

            idx += 1;
        }

        this.z_B0_w = this.markCoord[24 * 12].x - this.markCoord[0].x;

        let hh = (this.initialTime + this.addedTime) % 24;
        let tmstr = ('' + hh).padStart(2, '0') + ':00';

        this.markCoord.push({ 'x': this.borderLeft + timelineWidth, 'time': tmstr, 'idx': idx, 'w': 0, 'hour': hh, 'minutes': 0, 'today': false });

        this.z_B_x = this.z_A_w;
        this.z_B_w = this.markCoord[24 * 12].x - this.markCoord[0].x;
        this.z_C_x = this.z_A_w + this.z_B_w;
        this.z_C_w = this.canvasWidth - this.markCoord[24 * 12].x;


        //[ct, cv, ci, cm, cx, cw]
        this.cols.push(['A', null, 0, 1, 0, this.borderLeft])
        this.cols.push(['B', null, 0, 1, this.borderLeft, this.timelineWidth])


        this.z_s_y = this.z_r_h;
        this.z_s_h = Math.min(this.canvasHeight - this.z_s_y, this.maxHallHeight * this.halls.length);

        this.taskinfoshow = 3;
        if (this.z_s_h / Math.max(this.halls.length, 1) < 60) {
            this.taskinfoshow = 2;
        }
        if (this.z_s_h / Math.max(this.halls.length, 1) < 45) {
            this.taskinfoshow = 1;
        }
        if (this.z_s_h / Math.max(this.halls.length, 1) < 37) {
            this.taskinfoshow = 0;
        }

        idx = 0;
        for (let [y, h] of divideByInteger(this.z_s_h, this.halls.length)) {

            let hall = this.halls[idx];

            hall['y'] = y + this.z_r_h;
            hall['y2'] = y + h + this.z_r_h;
            hall['h'] = h;
            hall['idx'] = idx;

            this.rows.push(['s', hall, idx, this.halls.length, hall['y'], hall['h']]);

            idx += 1;
        }



        for (let ss of this.sprites) {
            ss.onLayout();
        }

        for (let ss of this.fixsprites) {
            ss.onLayout();
        }

    }

    onChangeCursorMode(mode) {

        this.cursor_mode = mode;

        if (this.cursor_mode == 'std') {
            this.spritedragable = true;
        }

        if (this.cursor_mode == 'add') {
            this.spritedragable = false;
        }

        if (this.cursor_mode == 'del') {
            this.spritedragable = false;
        }

    }

    draw(deep) {

        if (deep >= 0) {

            var ctx = this.layers[0].getContext('2d');

            if (this._dragOrClick == 'drag' && this._dragSprite) {

                ctx.fillStyle = 'rgba(0,0,0,0.15)';
                ctx.fillRect(this._dragSprite.x, this.z_r_h - 7, this._dragSprite.w, 7);

                ctx.strokeStyle = "#faa";

                ctx.beginPath();
                ctx.moveTo(this._dragSprite.x + 0.5, this.z_r_h - 20);
                ctx.lineTo(this._dragSprite.x + 0.5, this.z_r_h);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(this._dragSprite.x + 0.5, this.z_r_h - 20);
                ctx.lineTo(this._dragSprite.x + 0.5 - 3, this.z_r_h - 20 - 6.5);
                ctx.lineTo(this._dragSprite.x + 0.5 + 3, this.z_r_h - 20 - 6.5);
                ctx.closePath();
                ctx.stroke();

                ctx.fillStyle = '#f88';
                ctx.beginPath();
                ctx.moveTo(this._dragSprite.sx + 0.5, this.z_r_h);
                ctx.lineTo(this._dragSprite.sx + 0.5 - 3, this.z_r_h - 6.5);
                ctx.lineTo(this._dragSprite.sx + 0.5 + 3, this.z_r_h - 6.5);
                ctx.closePath();
                ctx.fill();
                ctx.strokeStyle = "#f88";
                ctx.beginPath();
                ctx.moveTo(this._dragSprite.sx, this.z_r_h - 0.5);
                ctx.lineTo(this._dragSprite.sx2, this.z_r_h - 0.5);
                ctx.stroke();

                ctx.font = '10px 微软雅黑';
                ctx.textBaseline = 'middle';
                ctx.fillStyle = "#f88";
                ctx.textAlign = 'left';

                ctx.fillText(this._dragSprite.startTime, this._dragSprite.x + 9, this.z_r_h - 20 - 4.5);

                ctx.strokeStyle = "#aaf";

                ctx.beginPath();
                ctx.moveTo(this._dragSprite.x2 + 0.5, this.z_r_h - 20);
                ctx.lineTo(this._dragSprite.x2 + 0.5, this.z_r_h);
                ctx.stroke();
                ctx.beginPath();
                ctx.moveTo(this._dragSprite.x2 + 0.5, this.z_r_h - 20);
                ctx.lineTo(this._dragSprite.x2 + 0.5 - 3, this.z_r_h - 20 - 6.5);
                ctx.lineTo(this._dragSprite.x2 + 0.5 + 3, this.z_r_h - 20 - 6.5);
                ctx.closePath();
                ctx.stroke();

                ctx.fillStyle = '#88f';
                ctx.beginPath();
                ctx.moveTo(this._dragSprite.sx2 + 0.5, this.z_r_h);
                ctx.lineTo(this._dragSprite.sx2 + 0.5 - 3, this.z_r_h - 6.5);
                ctx.lineTo(this._dragSprite.sx2 + 0.5 + 3, this.z_r_h - 6.5);
                ctx.closePath();
                ctx.fill();

                ctx.font = '10px 微软雅黑';
                ctx.textBaseline = 'middle';
                ctx.fillStyle = "#88f";
                ctx.textAlign = 'left';

                ctx.fillText(this._dragSprite.endTime, this._dragSprite.x + this._dragSprite.w + 9, this.z_r_h - 20 - 4.5);


                let lmt, rmt, lmm, rmm;
                [lmt, lmm, rmt, rmm] = this.nearestMovieTrack(this._dragSprite);
                if (lmt) {
                    this.drawDeltaTime(ctx, this._dragSprite.x, lmt.x + lmt.w, lmt.y + lmt.h, lmm);
                }

                if (rmt) {
                    this.drawDeltaTime(ctx, this._dragSprite.x + this._dragSprite.w, rmt.x, rmt.y + rmt.h, rmm);
                }

            } else if (this.curser_coord) {

                ctx.strokeStyle = "#faa";

                ctx.beginPath();
                ctx.moveTo(this.curser_coord.x + 0.5, this.z_r_h - 20);
                ctx.lineTo(this.curser_coord.x + 0.5, this.z_r_h);
                ctx.stroke();
                ctx.beginPath();
                ctx.arc(this.curser_coord.x + 0.5, this.z_r_h - 20 - 3, 3, 0, 2 * Math.PI);
                ctx.stroke();

                ctx.font = '10px 微软雅黑';
                ctx.textBaseline = 'middle';
                ctx.fillStyle = "#f88";
                ctx.textAlign = 'left';

                ctx.fillText(this.curser_coord.time, this.curser_coord.x + 9, this.z_r_h - 20 - 4.5);

            }

            if (this.cursor_mode == 'add') {

                if (this.curser_coord && this.curser_hall && this.new_program) {

                    let trackDummy = new MovieTrackBlock(this, this.new_program, this.curser_hall.idx, this.curser_coord.idx);
                    trackDummy.onLayout();

                    //let end_coord = this.markCoord[this.curser_coord.idx+90/5];
                    //let movietrack_w = end_coord.x - this.curser_coord.x;

                    ctx.fillStyle = 'rgba(0,0,0,0.15)';
                    //ctx.fillRect(this.curser_coord.x, this.z_r_h-7, movietrack_w, 7);
                    ctx.fillRect(trackDummy.x, this.z_r_h - 7, trackDummy.w, 7);


                    this.drawTrack(ctx, trackDummy);

                    let lmt, rmt, lmm, rmm;
                    [lmt, lmm, rmt, rmm] = this.nearestMovieTrack(trackDummy);
                    if (lmt) {
                        this.drawDeltaTime(ctx, trackDummy.x, lmt.x + lmt.w, lmt.y + lmt.h, lmm);
                    }

                    if (rmt) {
                        this.drawDeltaTime(ctx, trackDummy.x + trackDummy.w, rmt.x, rmt.y + rmt.h, rmm);
                    }

                    ctx.strokeStyle = "#aaf";

                    ctx.beginPath();
                    ctx.moveTo(trackDummy.x2 + 0.5, this.z_r_h - 20);
                    ctx.lineTo(trackDummy.x2 + 0.5, this.z_r_h);
                    ctx.stroke();
                    ctx.beginPath();
                    ctx.moveTo(trackDummy.x2 + 0.5, this.z_r_h - 20);
                    ctx.lineTo(trackDummy.x2 + 0.5 - 3, this.z_r_h - 20 - 6.5);
                    ctx.lineTo(trackDummy.x2 + 0.5 + 3, this.z_r_h - 20 - 6.5);
                    ctx.closePath();
                    ctx.stroke();

                    ctx.font = '10px 微软雅黑';
                    ctx.textBaseline = 'middle';
                    ctx.fillStyle = "#88f";
                    ctx.textAlign = 'left';

                    ctx.fillText(trackDummy.endTime, trackDummy.x2 + 9, this.z_r_h - 20 - 4.5);

                }

            }

            if (this.cursor_mode == 'del') {

                let s = this.hitTestSprites(this.curser_x, this.curser_y);

                if (s) {
                    ctx.fillStyle = "rgba(0,255,0,0.25)";
                    ctx.fillRect(s.x, s.y, s.w, s.h);
                }

            }


        }

        if (deep >= 1) {

            var ctx = this.layers[1].getContext('2d');

            for (let ss of this.sprites) {
                this.drawTrack(ctx, ss);
            }

        }

        if (deep >= 2) {
            var ctx = this.layers[2].getContext('2d');

            for (let ss of this.fixsprites) {
                this.drawTrack(ctx, ss, 1);
            }

        }

        if (deep >= 3) {

            var ctx = this.layers[3].getContext('2d');

            ctx.fillStyle = "#feffe8";
            ctx.fillRect(this.z_C_x, this.z_s_y, this.z_C_w, this.z_s_h);

            ctx.strokeStyle = "#eee";

            ctx.font = '14px 微软雅黑';
            ctx.textBaseline = 'middle';
            ctx.fillStyle = "#555";
            ctx.textAlign = 'center';

            ctx.beginPath();
            ctx.moveTo(0, this.z_r_h - 0.5);
            ctx.lineTo(this.canvasWidth, this.z_r_h - 0.5);
            ctx.stroke();

            for (let hall of this.halls) {

                ctx.beginPath();
                ctx.moveTo(0, hall['y2'] - 0.5);
                ctx.lineTo(this.canvasWidth, hall['y2'] - 0.5);
                ctx.stroke();

                ctx.fillText(hall.name, this.z_A_w / 2, hall['y'] + hall['h'] / 2);

            }


            ctx.beginPath();
            ctx.moveTo(this.borderLeft - 0.5, 50);
            ctx.lineTo(this.borderLeft - 0.5, this.canvasHeight);
            ctx.stroke();


            ctx.strokeStyle = "#aaa";

            ctx.font = '10px 微软雅黑';
            ctx.textBaseline = 'middle';
            ctx.fillStyle = "#555";
            ctx.textAlign = 'center';

            var time2x = new Map();


            for (let mc of this.markCoord) {

                ctx.strokeStyle = mc.today ? "#aaa" : "#eee";

                ctx.beginPath();
                let ly = -10;
                if (mc.minutes == 0) { ly = -20; }
                if (mc.minutes == 30) { ly = -15; }
                ctx.moveTo(mc.x + 0.5, this.z_r_h + ly);
                ctx.lineTo(mc.x + 0.5, this.z_r_h);
                ctx.stroke();

                if (mc.minutes == 0) {
                    ctx.fillText(mc.time, mc.x, this.z_r_h - 35);
                }

            }

            ctx.beginPath();
            ctx.moveTo(this.z_A_w, this.z_r_h - 0.5);
            ctx.lineTo(this.z_A_w + this.z_B_w, this.z_r_h - 0.5);
            ctx.stroke();

        }

        return;
    }

    onCursorMove(x, y) {

        this.curser_x = x;
        this.curser_y = y;

        let coord = null;
        if (this.curser_x > this.z_A_w && this.curser_x < this.z_A_w + this.z_B0_w) {
            coord = this.markCoord[this.x2mark[this.curser_x]];
        }

        let aimhall = null;

        for (let hall of this.halls) {
            if (this.curser_y > hall['y'] && this.curser_y < hall['y2']) {
                aimhall = hall;
            }
        }

        if (this.curser_coord != coord || this.cursor_hall != aimhall) {
            this.curser_coord = coord;
            this.curser_hall = aimhall;
            this.redraw(0);
        }

    }

    drawDeltaTime(ctx, x1, x2, y, deltatime) {

        ctx.strokeStyle = '#88f';
        ctx.beginPath();
        ctx.moveTo(x1, y + 10.5);
        ctx.lineTo(x1, y + 0.5);
        ctx.lineTo(x2, y + 0.5);
        ctx.stroke();

        ctx.beginPath();
        ctx.fillStyle = '#88f';
        ctx.arc(x2, y + 0.5, 2, 0, 2 * Math.PI);
        ctx.fill()

        ctx.font = '10px Verdana';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = "#88f";
        ctx.textAlign = (x1 > x2) ? 'right' : 'left';

        let xx = x1 + ((x1 > x2) ? -5 : 5);

        ctx.fillText('Δ' + deltatime + 'min', xx, y + 7);

    }

    drawTrack(ctx, track, colorType = 0) {

        //var hall = this.halls[track.hallid];

        var w = track.w;
        var h = track.h;

        var color = [{
            'blockStroke': '#ff4545',
            'blockFill': '#ffe8e8',
        }, {
            'blockStroke': '#454545',
            'blockFill': '#e8e8e8',
        }][colorType];


        ctx.save();
        ctx.translate(track.x, track.y);

        ctx.strokeStyle = color.blockStroke;
        ctx.fillStyle = color.blockFill;
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(w, 0);
        ctx.lineTo(w, h);
        ctx.lineTo(0, h);
        ctx.closePath();
        ctx.stroke();
        ctx.fill();

        ctx.save();
        ctx.rect(0, 0, w, h);
        ctx.clip();

        ctx.font = 'bold 14px 微软雅黑';
        ctx.textBaseline = 'middle';
        ctx.fillStyle = "#555";
        ctx.textAlign = 'left';

        var T = 5;
        var D = 4;
        var S = (T + D * this.taskinfoshow) * 2;

        ctx.fillText(track.data.film_name, 3, h * T / S);

        if (this.taskinfoshow >= 1) {
            ctx.font = '10px 微软雅黑';
            ctx.fillText('' + track.data.language + ' / ' + track.data.image, 3, h * (T * 2 + D) / S);
        }

        if (this.taskinfoshow >= 2) {
            ctx.font = '10px Verdana';
            ctx.fillText('' + track.startTime + '~' + track.endTime, 3, h * (T * 2 + D * 3) / S);
        }

        if (this.taskinfoshow >= 3) {
            ctx.font = '10px 黑体';
            ctx.fillText('[ ' + track.durationMinutes + '分钟 ]', 3, h * (T * 2 + D * 5) / S);
        }

        ctx.restore();
        ctx.restore();

    }

    hitTestMovieTrack(mt) {

        for (let s of[...this.sprites, ...this.fixsprites]) {

            if (s == mt) {
                continue;
            }

            if (s.hallidx != mt.hallidx) {
                continue;
            }

            if (mt.endMark <= s.startMark || mt.startMark >= s.endMark) {
                continue;
            } else {
                return s;
            }

        }

        return;
    }

    nearestMovieTrack(mt) {

        let lmt = null;
        let lmt_mark = 10;
        let rmt = null;
        let rmt_mark = 10;

        for (let s of[...this.sprites, ...this.fixsprites]) {

            if (s == mt) {
                continue;
            }

            if (s.hallidx != mt.hallidx) {
                continue;
            }

            if (s.endMark <= mt.startMark && (mt.startMark - s.endMark) <= lmt_mark) {
                lmt = s;
                lmt_mark = mt.startMark - s.endMark;
            }

            if (s.startMark >= mt.endMark && (s.startMark - mt.endMark) <= rmt_mark) {
                rmt = s;
                rmt_mark = s.startMark - mt.endMark;
            }

        }

        return [lmt, lmt_mark * 5, rmt, rmt_mark * 5];
    }

    onClick_sB(ct, cv, ci, cm, cx, cw, rt, rv, ri, rm, ry, rh, x, y) {

        if (this.cursor_mode == 'add') {

            let coord = null;
            if (this.curser_x > this.z_A_w && this.curser_x < this.z_A_w + this.z_B0_w) {
                coord = this.markCoord[this.x2mark[this.curser_x]];
            }

            if (coord && y > ry && y < ry + rh && this.new_program) {

                let mtb = new MovieTrackBlock(this, this.new_program, ri, coord.idx);

                if (!this.hitTestMovieTrack(mtb)) {
                    this.sprites.push(mtb);
                    mtb.onLayout();
                    this.redraw(1);

                }

            }

        } else if (this.cursor_mode == 'del') {
            let s = this.popHitSprites(x, y);
            if (s) {
                this.redraw(1);
            }
        }

    }

}


class LabelMarkGrid extends DataGrid {

    constructor() {
        super();
        this.prepare = [];
        this.flexible = true;
        this.clickable = true;
    }

    init(args) {

        this.blockSize = 20;
        this.maxBlock = { 'x': 60, 'y': 30 };
    }

    layout() {

        this.cols = [];
        this.rows = [];

        //[ct, cv, ci, cm, cx, cw]

        this.z_B_w = 50 * this.blockSize
        this.z_B_x = (this.canvasWidth - 50 * this.blockSize) / 2;
    }


    draw() {

        var ctx = this.can.getContext('2d');

        //ctx.fillStyle="#feffe8";
        //ctx.fillRect( this.z_C_x, this.z_s_y, this.z_C_w, this.z_s_h );

        ctx.strokeStyle = "#ccc";

        for (let bx = 1; bx <= this.maxBlock.x; bx++) {
            ctx.beginPath();
            ctx.moveTo(bx * this.blockSize + 0.5, 0);
            ctx.lineTo(bx * this.blockSize + 0.5, this.maxBlock.y * this.blockSize);
            ctx.stroke();
        }

        for (let by = 1; by <= this.maxBlock.y; by++) {
            ctx.beginPath();
            ctx.moveTo(0, by * this.blockSize + 0.5);
            ctx.lineTo(this.maxBlock.x * this.blockSize, by * this.blockSize + 0.5);
            ctx.stroke();
        }

    }

}


//var CanvasDataGrid = document.registerElement('ca-rolldatagrid', DataGrid);
//es6 need to use the blow to regist
window.customElements.define('ca-rolldatagrid', RollDataGrid);
window.customElements.define('hy-chaindate', StretchCheckGrid);
//window.customElements.define('hy-chainmonth', StretchCheckGrid2);
window.customElements.define('hy-chainboxoffice', StretchDataGrid);
window.customElements.define('ca-calendardata', CalendarGraphData);
window.customElements.define('hy-programdirector', TimelineTrack);
window.customElements.define('ca-labelgrid', LabelMarkGrid);