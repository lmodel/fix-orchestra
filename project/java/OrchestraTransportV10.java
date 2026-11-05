package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  The transport-level protocol of an interface or session, with its address, how messages are cast and its use.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraTransportV10 extends OrchestraProtocolV10 {

  private String fixiAddress;
  private String fixiMessageCast;
  private String fixiUse;


}