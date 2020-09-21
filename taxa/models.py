from django.db import models

from treebeard.mp_tree import MP_Node


class Division(models.Model):
    """
    This table represents the division/category that a node belongs to.
    It is populated using divisions.dmp file.
    """

    division_id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.code


class Node(MP_Node):
    """
    Table represents  a single node in am MPtree tree.
    In addition to the fields below path, depth, numchild are also available for each node.
    It is populated with nodes.dmp file.
    """

    tax_id = models.IntegerField(primary_key=True)
    rank = models.CharField(max_length=50)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __int__(self):
        return self.tax_id

    # def is_leaf(self):
    #     """ Returns True if leaf node else False"""
    #     print("HHH")
    #     return self.numchild == 0


class Name(models.Model):
    """"
    Tables denotes the different types of names associated with a taxid.
    It is populated using names.dmp file.
    """

    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    name_txt = models.CharField(max_length=50)
    unique_name = models.CharField(max_length=50)
    name_class = models.CharField(max_length=50)



    # class MPtree(MP_Node):
    #     name = models.CharField(max_length=30)
    #
    #     def __unicode__(self):
    #         return 'MPtree: %s' % self.name
    #
    # #
    # class NStree(NS_Node):
    #     name = models.CharField(max_length=30)
    #
    #     def __unicode__(self):
    #         return 'NStree: %s' % self.name
    #
    # class ALtree(AL_Node):
    #     name = models.CharField(max_length=30)
    #     parent = models.ForeignKey('self',
    #                                related_name='children_set',
    #                                null=True,
    #                                db_index=True,
    #                                on_delete=models.CASCADE)
    #     sib_order = models.PositiveIntegerField()
    #     desc = models.CharField(max_length=255)
    #
    #     def __unicode__(self):
    #         return 'ALtree: %s' % self.parent