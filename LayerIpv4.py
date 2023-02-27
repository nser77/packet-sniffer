class LayerIpv4(object):
  _format_string_="! 2x H H 2x B B H 4s 4s"

  def __init__(self, raw):
    """
      # 2s -> KO (version + ihl + tos)
        [actual 2x to skip fields]
      # H  -> OK (total length)
      # H  -> OK (identification)
      # 2s -> KO (flags + fragment offset)
         [actual 2x to skip fields]
      # B  -> OK (ttl)
      # B  -> OK (proto)
      # H  -> OK (header checksum)
      # 4s -> OK (src)
      # 4s -> OK (dst)
    """
    
    size = struct.calcsize(self._format_string_)

    # headers calc needed

    self.total_length, self.identification, self.ttl, self.proto, self.header_checksum, src, dst = struct.unpack(self._format_string_, raw[:size])
    self.src = self.formattedIpv4Address(src)
    self.dst = self.formattedIpv4Address(dst)

  def formattedIpv4Address(self, addr):
    return '.'.join(map(str, addr))
