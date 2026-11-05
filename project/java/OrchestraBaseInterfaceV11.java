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
  What an interface and a session share: the services, encodings and protocols of a connection, layer by layer.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class OrchestraBaseInterfaceV11  {

  private List<OrchestraServiceV11> fixiService;
  private List<OrchestraUserInterfaceV11> fixiUserInterface;
  private List<OrchestraEncodingV11> fixiEncoding;
  private List<OrchestraSessionProtocolV11> fixiSessionProtocol;
  private List<OrchestraProtocolV11> fixiProtocol;
  private List<OrchestraTransportV11> fixiTransport;
  private OrchestraInterfaceAnnotationV11 fixiAnnotation;
  private String fixiName;
  private List<OrchestraXmlAttribute> fixiOtherAttributes;


}