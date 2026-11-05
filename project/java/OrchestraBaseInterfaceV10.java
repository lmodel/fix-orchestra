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
  What an interface and a session share: the services, encodings and protocols that make up a connection, layer by layer.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class OrchestraBaseInterfaceV10  {

  private List<OrchestraServiceV10> fixiService;
  private List<OrchestraUserInterfaceV10> fixiUserInterface;
  private List<OrchestraEncodingV10> fixiEncoding;
  private List<OrchestraSessionProtocolV10> fixiSessionProtocol;
  private List<OrchestraProtocolV10> fixiProtocol;
  private List<OrchestraTransportV10> fixiTransport;
  private OrchestraInterfaceAnnotationV10 fixiAnnotation;
  private String fixiName;
  private List<OrchestraXmlAttribute> fixiOtherAttributes;


}