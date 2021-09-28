//console.log('Point of Sale JavaScript loaded');
odoo.define('pos_Coupons.custom',function (require) {
"use strict";

var screens = require('point_of_sale.models');
var rpc = require('web.rpc');
const Registries = require('point_of_sale.Registries');
//Modifying the POS screen UI
var pos_model = require('point_of_sale.models');
var CouponProductsPopup = require('pos_Coupons.CouponProductsPopup');
pos_model.load_fields("product.product",["qty_available","show_qty_on_hand","show_neg","can_still_sold_neg"]); //load standard_price field in js
//making business logic
const ProductScreen = require('point_of_sale.ProductScreen');
const PosComponentCoupon  = require('pos_Coupons.CouponButton');

const UpdatedProductScreen = ProductScreen =>
    class extends ProductScreen {
        _clickProduct(event) {
            const qty_product = event.detail
             super._clickProduct(event);

             this.showPopup('CouponProductsPopup', { title:'Do you want to add these Products?',
                                    body: '' });


        }
    };
    Registries.Component.extend(ProductScreen,UpdatedProductScreen);




});