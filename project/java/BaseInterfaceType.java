package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

@Data
@EqualsAndHashCode(callSuper=false)
public abstract class BaseInterfaceType  {

  private List<ServiceType> service;
  private List<UserInterfaceType> userInterface;
  private List<SessionProtocolType> sessionProtocol;
  private List<ProtocolType> protocol;
  private List<TransportProtocolType> transport;
  private List<String> extraAttributes;
  private List<EncodingType> encoding;
  private InterfaceAnnotation annotation;
  private String name;


}