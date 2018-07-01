

# ______________________________
# Dynamic module, concrete class

name1 = "pack1.class1"
mod1 = __import__(name1, fromlist=[""])
class1 = mod1.ClassOne()
print(class1.get_text())

# ______________________________
# Dynamic module, dynamic class

mod2 = __import__("pack2.concrete_class", fromlist=[""])
class2 = getattr(mod2, "ConcreteClass")()
print(class2.get_text())

# ______________________________
# All classes in module
# Available in Guitar Training Remote, look there