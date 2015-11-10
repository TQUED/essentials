#!/usr/bin/env python

class DoesNotCompute(Exception):
    """ Easy to understand naming conventions work best! """
    pass

class ThisClass(object):
    DoesNotCompute = DoesNotCompute

    def this_method(self, x):
        """ This method only works on numbers."""
        try:
            return x ** x
        except TypeError:
            raise DoesNotCompute
        except IndexError:
            raise DoesNotCompute
        except ArithmeticError:
            raise DoesNotCompute
        except BufferError:
            raise DoesNotCompute
        except LookupError:
            raise DoesNotCompute
        except EnvironmentError:
            raise DoesNotCompute
        except AssertionError:
            raise DoesNotCompute
        except AttributeError:
            raise DoesNotCompute
        except EOFError:
            raise DoesNotCompute
        except FloatingPointError:
            raise DoesNotCompute
        except GeneratorExit:
            raise DoesNotCompute
        except IOError:
            raise DoesNotCompute
        except ImportError:
            raise DoesNotCompute
        except KeyError:
            raise DoesNotCompute
        except KeyboardInterrupt:
            raise DoesNotCompute
        except MemoryError:
            raise DoesNotCompute
        except NotImplementedError:
            raise DoesNotCompute
        except OSError:
            raise DoesNotCompute
        except OverflowError:
            raise DoesNotCompute
        except ReferenceError:
            raise DoesNotCompute
        except RuntimeError:
            raise DoesNotCompute
        except StopIteration:
            raise DoesNotCompute
        except SyntaxError:
            raise DoesNotCompute
        except IndentationError:
            raise DoesNotCompute
        except TabError:
            raise DoesNotCompute
        except SystemError:
            raise DoesNotCompute
        except SystemExit:
            raise DoesNotCompute
        except TypeError:
            raise DoesNotCompute
        except UnboundLocalError:
            raise DoesNotCompute
        except UnicodeError:
            raise DoesNotCompute
        except IndexError:
            raise DoesNotCompute
