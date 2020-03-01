#
# This class is automatically generated by mig. DO NOT EDIT THIS FILE.
# This class implements a Python interface to the 'InitializationMsg'
# message type.
#

import tinyos.message.Message

# The default size of this message type in bytes.
DEFAULT_MESSAGE_SIZE = 8

# The Active Message type associated with this message.
AM_TYPE = 10

class InitializationMsg(tinyos.message.Message.Message):
    # Create a new InitializationMsg of size 8.
    def __init__(self, data="", addr=None, gid=None, base_offset=0, data_length=8):
        tinyos.message.Message.Message.__init__(self, data, addr, gid, base_offset, data_length)
        self.amTypeSet(AM_TYPE)
    
    # Get AM_TYPE
    def get_amType(cls):
        return AM_TYPE
    
    get_amType = classmethod(get_amType)
    
    #
    # Return a String representation of this message. Includes the
    # message type name and the non-indexed field values.
    #
    def __str__(self):
        s = "Message <InitializationMsg> \n"
        try:
            s += "  [UX=0x%x]\n" % (self.get_UX())
        except:
            pass
        try:
            s += "  [UY=0x%x]\n" % (self.get_UY())
        except:
            pass
        try:
            s += "  [ReplenishmentRate=0x%x]\n" % (self.get_ReplenishmentRate())
        except:
            pass
        try:
            s += "  [Type=0x%x]\n" % (self.get_Type())
        except:
            pass
        return s

    # Message-type-specific access methods appear below.

    #
    # Accessor methods for field: UX
    #   Field type: int
    #   Offset (bits): 0
    #   Size (bits): 16
    #

    #
    # Return whether the field 'UX' is signed (False).
    #
    def isSigned_UX(self):
        return False
    
    #
    # Return whether the field 'UX' is an array (False).
    #
    def isArray_UX(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'UX'
    #
    def offset_UX(self):
        return (0 / 8)
    
    #
    # Return the offset (in bits) of the field 'UX'
    #
    def offsetBits_UX(self):
        return 0
    
    #
    # Return the value (as a int) of the field 'UX'
    #
    def get_UX(self):
        return self.getUIntElement(self.offsetBits_UX(), 16, 1)
    
    #
    # Set the value of the field 'UX'
    #
    def set_UX(self, value):
        self.setUIntElement(self.offsetBits_UX(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'UX'
    #
    def size_UX(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'UX'
    #
    def sizeBits_UX(self):
        return 16
    
    #
    # Accessor methods for field: UY
    #   Field type: int
    #   Offset (bits): 16
    #   Size (bits): 16
    #

    #
    # Return whether the field 'UY' is signed (False).
    #
    def isSigned_UY(self):
        return False
    
    #
    # Return whether the field 'UY' is an array (False).
    #
    def isArray_UY(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'UY'
    #
    def offset_UY(self):
        return (16 / 8)
    
    #
    # Return the offset (in bits) of the field 'UY'
    #
    def offsetBits_UY(self):
        return 16
    
    #
    # Return the value (as a int) of the field 'UY'
    #
    def get_UY(self):
        return self.getUIntElement(self.offsetBits_UY(), 16, 1)
    
    #
    # Set the value of the field 'UY'
    #
    def set_UY(self, value):
        self.setUIntElement(self.offsetBits_UY(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'UY'
    #
    def size_UY(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'UY'
    #
    def sizeBits_UY(self):
        return 16
    
    #
    # Accessor methods for field: ReplenishmentRate
    #   Field type: int
    #   Offset (bits): 32
    #   Size (bits): 16
    #

    #
    # Return whether the field 'ReplenishmentRate' is signed (False).
    #
    def isSigned_ReplenishmentRate(self):
        return False
    
    #
    # Return whether the field 'ReplenishmentRate' is an array (False).
    #
    def isArray_ReplenishmentRate(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'ReplenishmentRate'
    #
    def offset_ReplenishmentRate(self):
        return (32 / 8)
    
    #
    # Return the offset (in bits) of the field 'ReplenishmentRate'
    #
    def offsetBits_ReplenishmentRate(self):
        return 32
    
    #
    # Return the value (as a int) of the field 'ReplenishmentRate'
    #
    def get_ReplenishmentRate(self):
        return self.getUIntElement(self.offsetBits_ReplenishmentRate(), 16, 1)
    
    #
    # Set the value of the field 'ReplenishmentRate'
    #
    def set_ReplenishmentRate(self, value):
        self.setUIntElement(self.offsetBits_ReplenishmentRate(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'ReplenishmentRate'
    #
    def size_ReplenishmentRate(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'ReplenishmentRate'
    #
    def sizeBits_ReplenishmentRate(self):
        return 16
    
    #
    # Accessor methods for field: Type
    #   Field type: int
    #   Offset (bits): 48
    #   Size (bits): 16
    #

    #
    # Return whether the field 'Type' is signed (False).
    #
    def isSigned_Type(self):
        return False
    
    #
    # Return whether the field 'Type' is an array (False).
    #
    def isArray_Type(self):
        return False
    
    #
    # Return the offset (in bytes) of the field 'Type'
    #
    def offset_Type(self):
        return (48 / 8)
    
    #
    # Return the offset (in bits) of the field 'Type'
    #
    def offsetBits_Type(self):
        return 48
    
    #
    # Return the value (as a int) of the field 'Type'
    #
    def get_Type(self):
        return self.getUIntElement(self.offsetBits_Type(), 16, 1)
    
    #
    # Set the value of the field 'Type'
    #
    def set_Type(self, value):
        self.setUIntElement(self.offsetBits_Type(), 16, value, 1)
    
    #
    # Return the size, in bytes, of the field 'Type'
    #
    def size_Type(self):
        return (16 / 8)
    
    #
    # Return the size, in bits, of the field 'Type'
    #
    def sizeBits_Type(self):
        return 16
    
