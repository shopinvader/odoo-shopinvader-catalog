# Copyright 2026 Akretion (http://www.akretion.com).
# @author Florian Mounier <florian.mounier@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo.tests.common import TransactionCase

from odoo.addons.extendable.tests.common import ExtendableMixin

from ..schemas import ProductHierarchicalCategory, ProductProduct


class TestHierarchicalCategoryInSchema(TransactionCase, ExtendableMixin):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.init_extendable_registry()
        cls.addClassCleanup(cls.reset_extendable_registry)

        cls.parent_category = cls.env["product.category"].create(
            {
                "name": "test parent category",
            }
        )
        cls.child_category = cls.env["product.category"].create(
            {
                "name": "test child category",
                "parent_id": cls.parent_category.id,
            }
        )
        cls.child_child_category = cls.env["product.category"].create(
            {
                "name": "test child child category",
                "parent_id": cls.child_category.id,
            }
        )
        cls.product = cls.env["product.product"].create(
            {
                "name": "test product",
                "categ_id": cls.child_child_category.id,
            }
        )

    def test_product_product(self):
        product = ProductProduct.from_product_product(self.product)
        self.assertEqual(len(product.hierarchicalCategories), 3)
        self.assertEqual(product.hierarchicalCategories[0].level, 1)
        self.assertEqual(
            product.hierarchicalCategories[0].value, "test parent category"
        )
        self.assertEqual(product.hierarchicalCategories[0].ancestors, [])
        self.assertEqual(product.hierarchicalCategories[1].level, 2)
        self.assertEqual(product.hierarchicalCategories[1].value, "test child category")
        self.assertEqual(
            product.hierarchicalCategories[1].ancestors, ["test parent category"]
        )
        self.assertEqual(product.hierarchicalCategories[2].level, 3)
        self.assertEqual(
            product.hierarchicalCategories[2].value, "test child child category"
        )
        self.assertEqual(
            product.hierarchicalCategories[2].ancestors,
            ["test child category", "test parent category"],
        )

    def test_product_hierarchical_category(self):
        hierarchical_category = ProductHierarchicalCategory.from_product_category(
            self.child_child_category
        )
        self.assertEqual(hierarchical_category.level, 3)
        self.assertEqual(hierarchical_category.value, "test child child category")
        self.assertEqual(
            hierarchical_category.ancestors,
            ["test child category", "test parent category"],
        )
