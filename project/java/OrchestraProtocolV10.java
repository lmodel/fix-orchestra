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
  A protocol used on one layer of an interface or session, with its version, layer and delivery guarantee.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraProtocolV10  {

  private OrchestraInterfaceAnnotationV10 fixiAnnotation;
  private String fixiName;
  private String fixiVersion;
  private String fixiLayer;
  private String fixiReliability;
  private URI fixiOrchestration;
  private List<OrchestraXmlAttribute> fixiOtherAttributes;


}